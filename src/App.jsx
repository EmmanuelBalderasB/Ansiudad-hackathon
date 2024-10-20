import React from "react";
import { useEffect, useState } from "react";

function app() {
  const generateEvents = document.getElementById("gen-events");
  const eventContainer = document.getElementById("event-container");
  const [events, setEvents] = React.useState("");

  async function getEvent(e) {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/generateEvents");
      const data = await response.json();
      console.log(data);
      eventContainer.innerText = data;
      return data;
    } catch (error) {
      console.log(error);
    }
  }
  return (
    <>
      <form action="get" class="w-1/2">
        <button
          type="submit"
          className="bg-green-300"
          id="gen-events"
          onClick={getEvent}
        >
          HIII
        </button>
      </form>
      <div id="event-container" className="w-1/2"></div>
    </>
  );
}

export default app;
