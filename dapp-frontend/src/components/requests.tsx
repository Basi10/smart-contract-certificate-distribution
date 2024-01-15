import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';

interface Feature {
  id: number;
  name: string;
}

const Features: React.FC = () => {
  const [features, setFeatures] = useState<Feature[]>([]);
  const location = useLocation();

  useEffect(() => {
    const searchParams = new URLSearchParams(location.search);
    const name = searchParams.get('name');

    if (name && !features.some((feature) => feature.name === name)) {
      const newFeature: Feature = {
        id: features.length + 1,
        name: name,
      };

      setFeatures([...features, newFeature]);
    }
  }, [location.search, features]);

  const handleAccept = (id: number) => {
    // Handle accept logic and send message to backend
    console.log(`Accept feature with id: ${id}`);
  };

  const handleReject = (id: number) => {
    // Handle reject logic and send message to backend
    console.log(`Reject feature with id: ${id}`);
  };

  return (
    <div>
      <h2>Requests</h2>
      <ul>
        {features.map((feature) => (
          <li key={feature.id}>
            <span>{feature.name}</span>
            <div>
              <button className='btn btn-success mr-2' onClick={() => handleAccept(feature.id)}>Accept</button>
              <button className='btn btn-danger' onClick={() => handleReject(feature.id)}>Reject</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Features;
