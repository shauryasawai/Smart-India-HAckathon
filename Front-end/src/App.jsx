import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from './signup';
import Login from './Login';
import Dashboard from './Dashboard';
import KnowledgeLevel from './KnowledgeLevel'; // Import the KnowledgeLevel component
import SkillAssessment from './SkillAssessment'

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/knowledge-level" element={<KnowledgeLevel />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/skillAssessment" element={<SkillAssessment />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;