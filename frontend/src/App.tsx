import React, { useState } from 'react';
import './App.css';

const BASE_API_URL = process.env.REACT_APP_BASE_API_URL || "http://127.0.0.1:8000";

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

      <p>{message}</p>
    </div>
  );
}

export default App;
