// App.tsx
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import axios from 'axios';
import NavBar from './components/navbar';
import Student from './components/student';


interface AppProps {}

const Home: React.FC = () => (
  <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h1>10 Academy</h1>
        <p>Which one are you?</p>
        <div>
          <Link to="/tutor">
            <button className="btn btn-dark mr-2">Tutor</button>
          </Link>
          <Link to="/student">
            <button className="btn btn-dark">Student</button>
          </Link>
        </div>
      </div>
    </div>

);




const App: React.FC<AppProps> = () => {
  const [userChoice, setUserChoice] = useState<string | null>(null);

  const handleButtonClick = async (choice: string) => {
    setUserChoice(choice);

    if (choice === 'option1') {
      try {
        console.log('Sending Axios request...');
        const response = await axios.post('http://localhost:5000/api/option1', { choice });
        console.log('Axios response:', response.data.message);
      } catch (error) {
        console.error('Error sending data to Flask:', error);

        if (axios.isAxiosError(error)) {
          console.error('AxiosError details:', error.response);
        }
      }
    }
  };

  return (
    <Router>
      <Routes>
        <Route path="/tutor" element={<NavBar />} />
        <Route path="/student" element={<Student />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
};

export default App;
