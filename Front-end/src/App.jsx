import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from './signup';
import Login from './Login';
import Dashboard from './Dashboard';
import SkillAssessment from './SkillAssessment'

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/skillAssessment" element={<SkillAssessment />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;