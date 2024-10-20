import React from "react";
import { Link } from "react-router-dom";
const Navbar = () => {
  return (
    <nav className="bg-yellow-300 shadow-md">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-center space-x-8 py-4 border">
          <Link
            to="/"
            className="text-gray-700 hover:text-gray-900 font-medium py-2 px-3"
          >
            ¿QUÉ ES ANSIUDAD?
          </Link>
          <Link
            to="/rules"
            className="text-gray-700 hover:text-gray-900 font-medium py-2 px-3"
          >
            REGLAS
          </Link>
          <Link
            to="/play"
            className="text-gray-700 hover:text-gray-900 font-medium py-2 px-3"
          >
            ¡QUIERO JUGAR!
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
