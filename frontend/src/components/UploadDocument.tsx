import { useState } from "react";
import { BASE_API_URL } from "../utils";

export function UploadDocument() {
  const [file, setFile] = useState<File | null>(null);

  async function uploadFile() {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(BASE_API_URL + "/documents/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log(data);
  }

  return (
    <div>
      <input
        type="file"
        accept=".txt,.pdf"
        onChange={(e) => setFile(e.target.files?.[0] ?? null)}
      />

      <button onClick={uploadFile}>
        Upload
      </button>
    </div>
  );
}