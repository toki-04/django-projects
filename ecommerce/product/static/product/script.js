let selected_size = ""
const quantity_counter = document.getElementById("quantity-counter")
let price = document.getElementById("price")

let base_price = price.innerText.replace("$", "").trim()
function add(){
  let current_value = parseInt(quantity_counter.innerText)
  let new_value = current_value + 1

  let new_price =  parseFloat(base_price * new_value).toFixed(2);

  quantity_counter.innerText = new_value
  price.innerText = new_price
}

function minus(){

  let current_value = parseInt(quantity_counter.innerText)

  if (current_value <= 1){
    return
  }

  let new_value = current_value - 1
  let new_price =  parseFloat(base_price * new_value).toFixed(2);

  quantity_counter.innerText = new_value
  price.innerText = new_price
}

let size_btn_container = document.getElementById("size-btn-container").childNodes
let children = []
for (let i=1; i<size_btn_container.length; i+=2){
  children.push(size_btn_container[i])
  if (i == 1){
    size_btn_container[i].className="active"

  }
}

children[0].addEventListener("click", function() {
  children[0].className="active"
  children[1].className=""
  children[2].className=""

  selected_size = children[0].innerText
})

children[1].addEventListener("click", function() {
  children[0].className=""
  children[1].className="active"
  children[2].className=""


  selected_size = children[1].innerText
})

children[2].addEventListener("click", function() {
  children[0].className=""
  children[1].className=""
  children[2].className="active"


  selected_size = children[2].innerText
})


api_url = "http://127.0.0.1:8000/cart/add-to-cart"
function add_to_cart(name, roast, price, image_url, created_by){
  size = selected_size
  quantity = quantity_counter.innerText

fetch(api_url, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "name":name,
      "roast":roast,
      "size":size,
      "quantity":quantity,
      "price": price,
      "image_url": image_url,
      "created_by": created_by, 
    })
})
   .then(response => response.json())
   .then(response => console.log(JSON.stringify(response)))

}
