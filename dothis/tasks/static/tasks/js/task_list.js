function bodyDropDown() {
  var body = document.getElementsByClassName("task-body");
  if (body.style.display[0] == "none") {
    body.style.display = "block";
  } else {
    body.style.display = "none";
  }
}
