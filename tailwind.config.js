/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        darkYellow: "##f3e29e",
      },
      backgroundImage: {
        fondo: "url('./static/FONDO.png')",
        animated: "url('./static/animated.gif')",
      },
    },
  },
  plugins: [],
};
