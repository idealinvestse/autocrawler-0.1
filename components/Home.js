import React, { useState } from 'react';
import axios from 'axios';

function Home() {
  const [status, setStatus] = useState('');

  const startCrawl = async () => {
    try {
      await axios.post('/start');
      setStatus('Crawling started');
    } catch (error) {
      setStatus('Error starting crawl');
    }
  };

  const checkStatus = async () => {
    try {
      const response = await axios.get('/status');
      setStatus(response.data.status);
    } catch (error) {
      setStatus('Error fetching status');
    }
  };

  const fetchResults = async () => {
    try {
      const response = await axios.get('/results');
      // Display results as needed
    } catch (error) {
      setStatus('Error fetching results');
    }
  };

  return (
    <div className="home">
      <button className="btn" onClick={startCrawl}>Start Crawl</button>
      <button className="btn" onClick={checkStatus}>Check Status</button>
      <button className="btn" onClick={fetchResults}>Fetch Results</button>
      <p>Status: {status}</p>
    </div>
  );
}

export default Home;