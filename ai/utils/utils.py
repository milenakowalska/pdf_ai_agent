from langchain.output_parsers import PydanticOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.runnables.passthrough import RunnableAssign
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel, Field
from typing import List

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", ";", ",", " ", ""],
)


class DocumentSummaryBase(BaseModel):
    running_summary: str = Field("", description="Running description of the document. Do not override; only update!")
    main_ideas: List[str] = Field([], description="Most important information from the document (max 3)")
    loose_ends: List[str] = Field([], description="Open questions that would be good to incorporate into summary, but that are yet unknown (max 3)")


def Extract(pydantic_class, llm, prompt):
    '''
    Runnable Extraction module
    Returns a knowledge dictionary populated by slot-filling extraction
    '''
    parser = PydanticOutputParser(pydantic_object=pydantic_class)
    instruct_merge = RunnableAssign({'format_instructions' : lambda x: parser.get_format_instructions()})
    def preparse(string):
        if '{' not in string: string = '{' + string
        if '}' not in string: string = string + '}'
        string = (string
            .replace("\\_", "_")
            .replace("\n", " ")
            .replace("\]", "]")
            .replace("\[", "[")
        )
        return string
    return instruct_merge | prompt | llm | preparse | parser

latest_summary = ""

def Summarizer(knowledge, llm, prompt):
    def summarize_docs(docs):        
        parse_chain = RunnableAssign({'info_base' : Extract(knowledge.__class__, llm, prompt)})
        state = {'info_base' : knowledge}
        
        for i, doc in enumerate(docs):
            state['input'] = doc.page_content
            state = parse_chain.invoke(state)

            assert 'info_base' in state 

        return state['info_base']
    
    return RunnableLambda(summarize_docs)

