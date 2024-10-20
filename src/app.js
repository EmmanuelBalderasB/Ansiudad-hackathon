const generateEvents = document.getElementById("gen-events");
const eventContainer = document.getElementById("event-container");
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

generateEvents.onclick = getEvent;
