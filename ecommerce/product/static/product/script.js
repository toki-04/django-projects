const quantity_counter = document.getElementById("quantity-counter")
const price = document.getElementById("price")

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
})

children[1].addEventListener("click", function() {
  children[0].className=""
  children[1].className="active"
  children[2].className=""
})

children[2].addEventListener("click", function() {
  children[0].className=""
  children[1].className=""
  children[2].className="active"
})

