// Bug 5: Misuse of types when adding shopping-cart prices.
// Intended: calculate the numerical sum of item prices.
function totalCart(prices) {
  let total = 0;
  for (const price of prices) {
    total += price;
  }
  return total;
}

const pricesFromForm = ["12", "8", "5"];
const result = totalCart(pricesFromForm);
console.log("Cart total:", result);
console.log("Expected cart total: 25");
