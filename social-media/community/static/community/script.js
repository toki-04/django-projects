function preview_image(){
  const image = document.getElementById("upload-image")
  const preview_img = document.getElementById("preview-img")

  const [file] = image.files

  preview_img.src = URL.createObjectURL(file)
  preview_img.style.display = "block"
}


