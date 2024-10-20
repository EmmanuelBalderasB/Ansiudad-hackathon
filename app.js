const div = document.getElementById("hello");

async function getEvent(e) {
  try {
    const response = await fetch("http://localhost:8000/getEvent");
    const data = await response.json();
    console.log(data);
    div.innerText = data;
    return data;
  } catch (error) {
    console.log(error);
  }
}

div.onclick = getEvent;
