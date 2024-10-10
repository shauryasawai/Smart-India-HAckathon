// KnowledgeAssessment.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const topics = ['Web Development', 'Data Science', 'Graphic Design', 'AI/ML', 'Marketing'];

const KnowledgeAssessment = () => {
  const navigate = useNavigate();
  const [knowledgeLevels, setKnowledgeLevels] = useState(
    topics.reduce((acc, topic) => {
      acc[topic] = 'Beginner'; // Default level for all topics
      return acc;
    }, {})
  );

  const handleLevelChange = (topic, level) => {
    setKnowledgeLevels({ ...knowledgeLevels, [topic]: level });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send the data with 'knowledge_levels' as the key
      await axios.post('http://localhost:8000/knowledge/', {
        knowledge_levels: knowledgeLevels,  // Make sure 'knowledgeLevels' is formatted properly in the state
      });
      alert('Knowledge levels saved successfully');
      navigate('/dashboard');
    } catch (error) {
      console.error('Error saving knowledge levels', error.response?.data || error.message);
      alert('Error saving knowledge levels: ' + JSON.stringify(error.response?.data));
    }
  };

  return (
    <div className="knowledge-assessment-container dark-theme">
      <h2>Set Your Current Knowledge Level</h2>
      <form onSubmit={handleSubmit}>
        {topics.map((topic) => (
          <div key={topic} className="topic">
            <h3>{topic}</h3>
            <div className="levels">
              {['Beginner', 'Intermediate', 'Advanced'].map((level) => (
                <label key={level}>
                  <input
                    type="radio"
                    name={topic}
                    value={level}
                    checked={knowledgeLevels[topic] === level}
                    onChange={() => handleLevelChange(topic, level)}
                  />
                  {level}
                </label>
              ))}
            </div>
          </div>
        ))}
        <button type="submit">Save Knowledge Levels</button>
      </form>
    </div>
  );
};

export default KnowledgeAssessment;
