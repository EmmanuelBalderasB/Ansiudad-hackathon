import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import About from "./components/About";
import Rules from "./components/Rules";
import Play from "./components/Play";

const App = () => {
  return (
    <Router>
      <div className="min-h-screen bg-yellow-200">
        <Navbar />
        <Routes>
          <Route path="/" element={<About />} />
          <Route path="/rules" element={<Rules />} />
          <Route path="/play" element={<Play />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
