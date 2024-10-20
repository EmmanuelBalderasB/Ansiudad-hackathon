import React, { useState } from "react";

const Play = () => {
  // Event states
  const [event, setEvent] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Roles states
  const [roles, setRoles] = useState(null);
  const [isRolesLoading, setIsRolesLoading] = useState(false);
  const [errorRoles, setErrorRoles] = useState(null);

  const getEvent = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch("http://localhost:8000/generateEvents");
      if (!response.ok) {
        throw new Error("Failed to fetch event");
      }
      const data = await response.json();
      setEvent(data);
    } catch (error) {
      setError(error.message);
      console.error("Error fetching event:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const getRoles = async (e) => {
    e.preventDefault();
    setIsRolesLoading(true);
    setErrorRoles(null);

    try {
      const response = await fetch("http://localhost:8000/generateRoles", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ number: 5 }),
      });
      if (!response.ok) {
        throw new Error("Failed to fetch roles");
      }
      const data = await response.json();
      setRoles(data);
      console.log(data);
    } catch (error) {
      setErrorRoles(error.message);
      console.error("Error fetching roles:", error);
    } finally {
      setIsRolesLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="max-w-7xl mx-auto px-4">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">
          Genrador de Incidente y Roles
        </h1>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Event Generator Section */}
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-6 text-gray-800">
              Generar Incidente
            </h2>
            <div className="max-w-2xl mx-auto">
              <form onSubmit={getEvent} className="mb-4">
                <button
                  type="submit"
                  className="w-full bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded disabled:opacity-50 disabled:cursor-not-allowed transition duration-150"
                  disabled={isLoading}
                >
                  {isLoading ? "Generating Event..." : "Generate New Event"}
                </button>
              </form>

              {error && (
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                  Error: {error}
                </div>
              )}

              {event && (
                <div className="bg-gray-50 rounded-lg overflow-hidden border border-gray-200">
                  <div className="p-6">
                    <h3 className="text-xl font-bold mb-4 text-gray-800">
                      {event}
                    </h3>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Roles Generator Section */}
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-6 text-gray-800">
              Roles Generator
            </h2>
            <div className="max-w-2xl mx-auto">
              <form onSubmit={getRoles} className="mb-4">
                <button
                  type="submit"
                  className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded disabled:opacity-50 disabled:cursor-not-allowed transition duration-150"
                  disabled={isRolesLoading}
                >
                  {isRolesLoading ? "Generating Roles..." : "Generate 5 Roles"}
                </button>
              </form>

              {errorRoles && (
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                  Error: {errorRoles}
                </div>
              )}

              {roles && (
                <div className="bg-gray-50 rounded-lg overflow-hidden border border-gray-200">
                  <div className="p-6">
                    <div className="space-y-4">
                      {Array.isArray(roles) ? (
                        roles.map((role, index) => (
                          <div
                            key={index}
                            className="p-3 bg-white rounded shadow"
                          >
                            <h3 className="font-semibold text-gray-800">
                              Role {index + 1}
                            </h3>
                            <p className="text-gray-600">{role}</p>
                          </div>
                        ))
                      ) : (
                        <div className="p-3 bg-white rounded shadow">
                          <p className="text-gray-600">
                            {JSON.stringify(roles)}
                          </p>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Play;
