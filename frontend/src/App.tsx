import React, { useState } from 'react';
import './App.css';
import { BASE_API_URL } from "./utils";
import { UploadDocument } from './components/UploadDocument';

console.log("base url", BASE_API_URL)

function App() {
  const [message, setMessage] = useState("");

  const callBackend = async () => {
    try {
      const response = await fetch(BASE_API_URL);

      const data = await response.json();

      setMessage(data.message);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Homepage</h1>
      <button onClick={callBackend}>
        Call Backend
      </button>
      <UploadDocument />

      <p>{message}</p>
    </div>
  );
}

export default App;
