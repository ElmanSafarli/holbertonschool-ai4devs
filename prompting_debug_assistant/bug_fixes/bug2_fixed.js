// Fixed Bug 2: subtract the discount rather than add it.
function finalPrice(price, discP) {
    const discount = price * (discP / 100);
    const finalPrice = price - discount;
    return finalPrice;
}

const products = [
    {name: "book", price: 20, discount: 10},
    {name: "book", price: 1000, discount: 20},
];

for (const product of products) {
    const total = finalPrice(product.price, product.discount);
    console.log(`${product.name}: $${total.toFixed(2)}`);
}
