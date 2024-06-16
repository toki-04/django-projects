const modal = document.getElementById("modal")
function close_modal(){
  modal.style.display = "none"
  document.body.className = ""
}

function open_modal(){
  modal.style.display = "flex"
  document.body.className = "stop-scrolling"
}
