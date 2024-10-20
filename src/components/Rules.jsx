import React from "react";
const Rules = () => {
  return (
    <div className="min-h-screen bg-fondo bg-cover py-8">
      <div className="max-w-4xl mx-auto px-4">
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h2 className="text-3xl font-bold mb-6 text-gray-800">
            ¿CÓMO SE JUEGA?
          </h2>
          <div className="space-y-4">
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-lg mb-2">1. FORMA TU EQUIPO</h3>
              <p className="text-gray-600">
                Pueden jugar de 3 a 6 equipos de máximo 10 integrantes.
              </p>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-lg mb-2">
                2. Asignación de roles
              </h3>
              <p className="text-gray-600">
                Ingresa la cantidad de jugadores. Nuestra plataforma asignará a
                cada unx un rol que deberán adoptar durante el juego. Cada
                jugador tendrá prioridades y motivaciones específicas que debe
                proteger en relación con lxs demás jugadores.
              </p>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-lg mb-2">3. Interaccion</h3>
              <p className="text-gray-600">
                Puedes generar cuantos eventos y rolos que desees gracias al
                poder del LLM LLAMA 3.2 hecho por Meta
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Rules;
