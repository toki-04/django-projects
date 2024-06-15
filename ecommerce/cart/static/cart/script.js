api_url = "http://127.0.0.1:8000/cart/add-to-cart"
function add_to_cart(id, name, roast, size, quantity, price, created_at, created_by){
fetch(api_url, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "id": id,
      "name":name,
      "roast":roast,
      "size":size,
      "quantity":quantity,
      "price": price,
      "created_at": created_at,
      "created_by": created_by, 
    })
})
   .then(response => response.json())
   .then(response => console.log(JSON.stringify(response)))
}
