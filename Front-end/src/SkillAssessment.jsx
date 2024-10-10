// SkillAssessment.js
import React, { useState } from 'react';
import axios from 'axios';

const SkillAssessment = () => {
  const [answers, setAnswers] = useState([]);
  const [score, setScore] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/skill-assessment/', {
        answers,
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`,  // JWT token
        },
      });
      setScore(response.data.score);
    } catch (error) {
      console.error('Error submitting skill assessment', error);
    }
  };

  return (
    <div className="assessment-container dark-theme">
      <h2>Skill Assessment</h2>
      {/* Render a few sample questions */}
      <form onSubmit={handleSubmit}>
        {/* Simplified example of rendering quiz questions */}
        <div>
          <label>Question 1: 2+2 = ?</label>
          <input type="number" onChange={(e) => setAnswers([Number(e.target.value)])} required />
        </div>
        <button type="submit">Submit</button>
      </form>

      {score !== null && <h3>Your Score: {score}</h3>}
    </div>
  );
};

export default SkillAssessment;
