// App.tsx
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

interface AppProps {}

const App: React.FC<AppProps> = () => {
  const [userChoice, setUserChoice] = useState<string | null>(null);

  const handleButtonClick = async (choice: string) => {
    setUserChoice(choice);
  
    if (choice === 'option1') {
      try {
        // Log the request details for debugging
        console.log('Sending Axios request...');
        const response = await axios.post('http://localhost:5000/api/option1', { choice });
        console.log('Axios response:', response.data.message);
      } catch (error) {
        console.error('Error sending data to Flask:', error);
  
        // Log specific Axios error details
        if (axios.isAxiosError(error)) {
          console.error('AxiosError details:', error.response);
        }
      }
    }
  };
  

  return (
    <div className="App">
      <h1>Welcome to Your App</h1>
      <p>Please choose one of the following options:</p>

      <div>
        <button onClick={() => handleButtonClick('option1')}>Option 1</button>
      </div>

      {userChoice && (
        <p>You chose: {userChoice}</p>
      )}
    </div>
  );
};

export default App;
