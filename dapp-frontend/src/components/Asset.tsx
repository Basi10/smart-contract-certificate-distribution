// Home.tsx
import React, { useState } from 'react';

const Home: React.FC = () => {
  const [inputValues, setInputValues] = useState({
    value1: '',
    value2: '',
    value3: '',
    value4: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>, fieldName: string) => {
    setInputValues({
      ...inputValues,
      [fieldName]: e.target.value,
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Add your logic here to send inputValues to the backend
    console.log('Sending values to backend:', inputValues);
  };

  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h2>Create Certificate</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group row mt-4">
            <label htmlFor="value1" className="col-sm-2 col-form-label">
              Trainee Name:
            </label>
            <div className="col-sm-4">
              <input
                type="text"
                className="form-control"
                id="value1"
                value={inputValues.value1}
                onChange={(e) => handleChange(e, 'value1')}
              />
            </div>
            <label htmlFor="value2" className="col-sm-2 col-form-label">
              Trainee Email:
            </label>
            <div className="col-sm-4">
              <input
                type="text"
                className="form-control"
                id="value2"
                value={inputValues.value2}
                onChange={(e) => handleChange(e, 'value2')}
              />
            </div>
          </div>
          <div className="form-group row mt-4">
            <label htmlFor="value3" className="col-sm-2 col-form-label">
              Public Key:
            </label>
            <div className="col-sm-4">
              <input
                type="text"
                className="form-control"
                id="value3"
                value={inputValues.value3}
                onChange={(e) => handleChange(e, 'value3')}
              />
            </div>
            <label htmlFor="value4" className="col-sm-2 col-form-label">
              Private Key:
            </label>
            <div className="col-sm-4">
              <input
                type="text"
                className="form-control"
                id="value4"
                value={inputValues.value4}
                onChange={(e) => handleChange(e, 'value4')}
              />
            </div>
          </div>
          <div className="form-group row mt-4">
            <div className="col-sm-10 offset-sm-2">
              <button type="submit" className="btn btn-dark">
                Create
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Home;
