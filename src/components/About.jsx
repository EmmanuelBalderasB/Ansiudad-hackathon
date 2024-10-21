import React from "react";

const About = () => {
  return (
    <div className="min-h-screen bg-fondo bg-cover py-8  justify-center">
      <div className="max-w-4xl mx-auto px-4">
        <div className="bg-white rounded-lg shadow-lg p-8 mt-32">
          <h2 className="text-3xl font-bold mb-6 text-gray-800">
            ¿QUÉ ES ANSIUDAD?
          </h2>
          <div className="prose max-w-none">
            <p className="text-gray-600">
              Es un mega juego que tiene el objetivo de fomentar conversaciones
              desde un enfoque de diseño social, promoviendo el pensamiento
              creativo e inclusivo que pueda llevarnos a futuros más sostenibles
              y equitativos. Los problemas socioambientales son tan complejos
              que como ciudadanxs, parecen imposibles de resolver. Ansiudad
              busca acortar la brecha entre las personas y los grandes retos del
              planeta a través del juego serio.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
