"use strict";

// Exercise: return the sum of all line-item totals.
function cartTotal(items) {
  let total = 0;
  for (let i = 0; i < items.length - 1; i += 1) {
    total += items[i].price * items[i].quantity;
  }
  return total;
}

const cart = [
  { price: 10, quantity: 2 },
  { price: 5, quantity: 3 },
];
console.log(cartTotal(cart));
module.exports = { cartTotal };
