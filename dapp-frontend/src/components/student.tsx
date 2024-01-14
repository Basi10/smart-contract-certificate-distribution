import React, { useState, ChangeEvent, FormEvent } from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap styles

interface FormData {
  inputValue: string;
}

function Student() {
  const [formData, setFormData] = useState<FormData>({
    inputValue: '',
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // Send formData to the backend here
    console.log('Form data submitted:', formData);
  };

  return (
    <div className="d-flex flex-column" style={{ minHeight: '100vh' }}>
      <div className="p-3">
        <Link to="/" className="btn btn-outline-secondary">&larr; </Link>
      </div>
      <div className="flex-grow-1 d-flex flex-column align-items-center justify-content-center">
        <h2 className="mb-4">Student Page - Hello World!</h2>
        <form onSubmit={handleSubmit} className="d-flex flex-column align-items-start">
          <div className="form-group d-flex">
            <label htmlFor="inputValue" className="mr-2">Input Label:</label>
            <input
              type="text"
              className="form-control"
              id="inputValue"
              name="inputValue"
              value={formData.inputValue}
              onChange={handleChange}
            />
          </div>
          <div className="form-group ml-auto mt-2">
            <button type="submit" className="btn btn-dark">Submit</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Student;
