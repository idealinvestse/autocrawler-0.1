import React from 'react';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Console from './components/Console';
import Metrics from './components/Metrics';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="container mx-auto">
        <Home />
        <Console />
        <Metrics />
      </div>
    </div>
  );
}

export default App;