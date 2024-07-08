import React from 'react';

function Navbar() {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto">
        <a href="/" className="text-white">Home</a>
        <a href="/console" className="text-white ml-4">Console</a>
        <a href="/metrics" className="text-white ml-4">Metrics</a>
      </div>
    </nav>
  );
}

export default Navbar;