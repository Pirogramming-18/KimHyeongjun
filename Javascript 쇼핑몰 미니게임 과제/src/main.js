// Fetch the items from the JSON file
function loadItems() {
  return fetch("data/data.json")
    .then((response) => response.json())
    .then((json) => json.items);
}

// main
loadItems()
  .then((items) => {
    console.log(item);
    // displayItems(items);
    // setEventListensers(items);
  })
  .catch(console.log);
