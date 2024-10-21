import React from "react";
import { Link } from "react-router-dom";
const Navbar = () => {
  return (
    <nav className="bg-yellow-300 shadow-md w-screen pt-2 flex flex-row">
      <div className="w-1/3 h-16 bg-animated bg-cover"></div>
      <div className="max-w-7xl mx-0 px-4">
        <div className="flex justify-center space-x-8 py-3 mx-4">
          <Link
            to="/"
            className="text-black rounded hover:text-white hover:bg-purple-700 ease-in duration-200 font-medium py-4 px-3"
          >
            ¿QUÉ ES ANSIUDAD?
          </Link>
          <Link
            to="/rules"
            className="text-black rounded hover:text-white hover:bg-purple-700 ease-in duration-200 font-medium py-4 px-3"
          >
            REGLAS
          </Link>
          <Link
            to="/play"
            className="text-black rounded hover:text-white hover:bg-purple-700 ease-in duration-200 font-medium py-4 px-3"
          >
            ¡QUIERO JUGAR!
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
