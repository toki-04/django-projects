function like_post(){
  const likes_document = document.getElementById("likes")
  const likes_img = document.getElementById("likes-img")
  
  likes = parseInt(likes_document.innerText);
  likes += 1
  likes_document.innerText = likes
  likes_img.src = "/static/core/images/heart-filled.png"
}
