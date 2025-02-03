document.getElementById("todo").addEventListener("drop", (ev) => dropHandler(ev, "todo"))
document.getElementById("done").addEventListener("drop", (ev) => dropHandler(ev, "done"))
document.getElementById("approved").addEventListener("drop", (ev) => dropHandler(ev, "approved"))

function dragstartHandler(ev) {
  ev.dataTransfer.setData("text/plain", ev.target.id);
  const cardWrappers = document.getElementsByClassName("cards-wrapper");
  Array.from(cardWrappers).forEach((c) => {
    c.classList.add("card-placeable");
  });
}

function dragendHandler(ev) {
  const cardWrappers = document.getElementsByClassName("cards-wrapper");
  Array.from(cardWrappers).forEach((c) => {
    c.classList.remove("card-placeable");
  });
}

function dragoverHandler(ev) {
  ev.preventDefault();
  ev.dataTransfer.dropEffect = "move";
}

function dropHandler(ev, columnId) {
  ev.preventDefault();
  const card = ev.dataTransfer.getData("text/plain");
  const column = document.getElementById(columnId);
  console.log(column);
  column.appendChild(document.getElementById(card));
}