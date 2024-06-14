const item_container = document.getElementById("item-container");
let product_list = []
let roast_id = 0
let size_id = 0
let coffee_type_id = 0
let api_url = "http://127.0.0.1:8000/api/product/"



async function fetch_product(url){
  const response = await fetch(url);
  return await response.json();
}


function create_product(product_list){
  item_container.innerHTML = ""
  for (let i=0; i<product_list.length; i++){
    const item = document.createElement("a");
    const image = document.createElement("img");
    const name = document.createElement("h3");
    const price = document.createElement("h3");

    item.setAttribute("class", "item")
    item.setAttribute("href", `http://127.0.0.1:8000/product/`+product_list[i].id)

    image.setAttribute("src", product_list[i].image)
    name.innerText = product_list[i].name

    price.setAttribute("class", "price")
    price.innerText = "$ "+product_list[i].price

    item.appendChild(image)
    item.appendChild(name)
    item.appendChild(price)
    item_container.appendChild(item)
  }
}

async function get_all_products(){
  let arr = []
  await fetch_product(api_url).then(data => {
    for (let i=0; i<data.length;i++){
      arr.push(data[i])
    }

  })
  return arr
}

function filter_buttons(element_id, id){
  let id_counter = 0
  const container = document.getElementById(element_id).childNodes

  for (let i=1; i<container.length; i+=2){
    let children = container[i]
    id === id_counter ? children.className="active" : children.className=""
    id_counter += 1
  }
}

function filter_roast(id){
  roast_id = id
  filter_buttons("roast-container", roast_id)
  filtered_products(roast_id, size_id, coffee_type_id)


}

function filter_size(id){
  size_id = id
  filter_buttons("size-container", size_id)
  filtered_products(roast_id, size_id, coffee_type_id)
}

function filter_coffee_type(id){
  coffee_type_id = id
  filter_buttons("filter-coffee-container", coffee_type_id)
  filtered_products(roast_id, size_id, coffee_type_id)
}

function filtered_products(roast_id, size_id, coffee_type_id){
  get_all_products().then(data => {
    roast_arr = []
    for (let i=0; i<data.length; i++){
      if (roast_id && data[i].roast.includes(roast_id)){
        roast_arr.push(data[i])
      }
      else if (roast_id === 0){
        roast_arr = data
      }
    }

    size_arr = []
    for (let i=0; i<roast_arr.length; i++){
      if (size_arr && roast_arr[i].size.includes(size_id)){
        size_arr.push(roast_arr[i])
      }
      else if(size_id === 0){
        size_arr = roast_arr
      }

    }

    coffee_type_arr = []
    for (let i=0; i<size_arr.length; i++){
      if (coffee_type_id && size_arr[i].coffee_type.includes(coffee_type_id)){
        coffee_type_arr.push(size_arr[i])
      }
      else if(coffee_type_id === 0){
        coffee_type_arr = size_arr
      }
    }

    let filtered_arr = coffee_type_arr

    create_product(filtered_arr)
  })




}

get_all_products().then(data => {
  create_product(data)
})

function filter_options(){
  const filter_options = document.getElementById("filter-options")
  const value = filter_options.value
  const FEATURED = "featured"
  const HIGH_TO_LOW = "high-to-low"
  const LOW_TO_HIGH = "low-to-high"

  if (value == FEATURED){
    get_all_products().then(data => {
      create_product(data)
    })
  }

}
const roast_filter = document.getElementById("roast-filter")
roast_filter.addEventListener("change", function(){
  roast_id = parseInt(roast_filter.value);
  filtered_products(roast_id, size_id, coffee_type_id)
})

const size_filter = document.getElementById("size-filter")
size_filter.addEventListener("change", function(){
  size_id= parseInt(size_filter.value);
  filtered_products(roast_id, size_id, coffee_type_id)
})

const coffee_type_filter = document.getElementById("coffee-type-filter")
coffee_type_filter.addEventListener("change", function(){
  coffee_type_id = parseInt(coffee_type_filter.value);
  filtered_products(roast_id, size_id, coffee_type_id)
})




