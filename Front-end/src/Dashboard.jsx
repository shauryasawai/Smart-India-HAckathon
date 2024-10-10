// Dashboard.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [userInfo, setUserInfo] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const accessToken = localStorage.getItem('access');
        const response = await axios.get('http://localhost:8000/auth/users/me/', {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });
        setUserInfo(response.data);
      } catch (error) {
        setError('Failed to fetch user data. Please log in again.');
        console.error('Error fetching user data', error);
      }
    };

    fetchUserData();
  }, []);

  return (
    <div className="dashboard-container dark-theme">
      <h2>Welcome to Your Dashboard</h2>
      {error && <p className="error-message">{error}</p>}
      {userInfo ? (
        <div>
          <h3>User Information</h3>
          <p><strong>Username:</strong> {userInfo.username}</p>
          <p><strong>Email:</strong> {userInfo.email}</p>
          <p><strong>Interests:</strong> {userInfo.interests.join(', ')}</p>
          <p><strong>Initial Score:</strong> {userInfo.initial_score}</p>
          {/* Add more user-related information as needed */}
        </div>
      ) : (
        <p>Loading user data...</p>
      )}
    </div>
  );
};

export default Dashboard;
