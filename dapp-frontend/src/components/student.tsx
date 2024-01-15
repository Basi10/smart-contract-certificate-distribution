import React, { useState, ChangeEvent, FormEvent } from 'react';
import { Link } from 'react-router-dom';

interface FormData {
  inputValue1: string;
  inputValue2: string;
  inputValue3: string;
}

function Student() {
  const [formData, setFormData] = useState<FormData>({
    inputValue1: '',
    inputValue2: '',
    inputValue3: '',
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // Access the name value from formData
    const { inputValue1 } = formData;

    // Redirect to the Features page with the entered name
    window.location.href = `/tutor?name=${inputValue1}`;
  };

  return (
    <div className="d-flex flex-column" style={{ minHeight: '100vh' }}>
      <div className="p-3">
        <Link to="/" className="btn btn-outline-secondary">&larr; </Link>
      </div>
      <div className="flex-grow-1 d-flex flex-column align-items-center justify-content-center">
        <h2 className="mb-4">Student Page - Hello World!</h2>
        <form onSubmit={handleSubmit} className="d-flex flex-column align-items-start">
          {/* Form 1 */}
          <div className="form-group d-flex mt-4">
            <label htmlFor="inputValue1" className="mr-2">Name:</label>
            <input
              type="text"
              className="form-control"
              id="inputValue1"
              name="inputValue1"
              value={formData.inputValue1}
              onChange={handleChange}
            />
          </div>

          {/* Form 2 */}
          <div className="form-group d-flex mt-4">
            <label htmlFor="inputValue2" className="mr-2">Asset id:</label>
            <input
              type="text"
              className="form-control"
              id="inputValue2"
              name="inputValue2"
              value={formData.inputValue2}
              onChange={handleChange}
            />
          </div>

          {/* Form 3 */}
          <div className="form-group d-flex mt-4">
            <label htmlFor="inputValue3" className="mr-2">Private Key:</label>
            <input
              type="text"
              className="form-control"
              id="inputValue3"
              name="inputValue3"
              value={formData.inputValue3}
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
