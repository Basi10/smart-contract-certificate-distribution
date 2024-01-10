import React, { useState } from 'react';
import './App.css';

interface AppProps {}

const App: React.FC<AppProps> = () => {
  // State to track the user's choice
  const [userChoice, setUserChoice] = useState<string | null>(null);

  // Function to handle button clicks
  const handleButtonClick = (choice: string) => {
    setUserChoice(choice);
    // You can add logic here to navigate to the next page or perform other actions based on the user's choice
  };

  return (
    <div className="App">
      <h1>Welcome to 10 Academy Certificate Site</h1>
      <p>Please select if you are a tutor or a trainee :</p>

      <div>
        <button onClick={() => handleButtonClick('option1')}>Tutor</button>
        <button onClick={() => handleButtonClick('option2')}>Trainee</button>
      </div>

      {userChoice && (
        <p>You chose: {userChoice}</p>
        // You can render different components or navigate to different pages based on the user's choice
      )}
    </div>
  );
};

export default App;
