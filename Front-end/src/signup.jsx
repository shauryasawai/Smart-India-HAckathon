// Signup.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const Signup = () => {
  const navigate = useNavigate(); // Initialize the useNavigate hook
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: '',
    interests: [],
  });

  const interestsOptions = [
    'Web Development',
    'Data Science',
    'Graphic Design',
    'AI/ML',
    'Marketing',
  ];

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleCheckboxChange = (interest) => {
    const newInterests = formData.interests.includes(interest)
      ? formData.interests.filter((i) => i !== interest)
      : [...formData.interests, interest];
    setFormData({ ...formData, interests: newInterests });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send signup data to the backend
      await axios.post('http://localhost:8000/auth/users/', formData);
      alert('User registered successfully');

      // Redirect to the login page
      navigate('/login'); // Use the navigate function to redirect
    } catch (error) {
      console.error('Error registering user', error);
      alert('Error registering user: ' + (error.response?.data?.detail || error.message));
    }
  };

  return (
    <div className="signup-container dark-theme">
      <h2>Create an Account</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          onChange={handleChange}
          required
        />

        <h3>Select Areas of Interest</h3>
        <div className="interests-options">
          {interestsOptions.map((interest) => (
            <label key={interest}>
              <input
                type="checkbox"
                value={interest}
                onChange={() => handleCheckboxChange(interest)}
                checked={formData.interests.includes(interest)}
              />
              {interest}
            </label>
          ))}
        </div>

        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default Signup;
