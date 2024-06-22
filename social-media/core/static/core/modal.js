const modal = document.getElementById("modal")
function close_modal(){
  modal.style.display = "none"
  document.body.className = ""
}

function open_modal(){
  modal.style.display = "flex"
  document.body.className = "stop-scrolling"
}

function modal_preview_image(){
  const image = document.getElementById("modal-upload-image")
  const preview_img = document.getElementById("modal-preview-img")

  const [file] = image.files

  preview_img.src = URL.createObjectURL(file)
  preview_img.style.display = "block"
}
