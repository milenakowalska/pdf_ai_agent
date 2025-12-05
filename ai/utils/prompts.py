from langchain_core.prompts import ChatPromptTemplate

summary_prompt = ChatPromptTemplate.from_template(
    "You are generating a running summary of the document. Make it readable by a technical user."
    " After this, the old knowledge base will be replaced by the new one. Make sure a reader can still understand everything."
    " Keep it short, but as dense and useful as possible! The information should flow from chunk to (loose ends or main ideas) to running_summary."
    " The updated knowledge base keep all of the information from running_summary here: {info_base}."
    "\n\n{format_instructions}. Follow the format precisely, including quotations and commas. "
    "Return ONLY JSON in the given format. No additional comments or text outside JSON."
    "\n\nWithout losing any of the info, update the knowledge base with the following: {input}"
)