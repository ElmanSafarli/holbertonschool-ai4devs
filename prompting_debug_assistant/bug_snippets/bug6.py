# Bug 6: Runtime error from modifying a dictionary during iteration.
# Intended: remove all entries whose stock is zero.

def remove_out_of_stock(inventory):
    for item, quantity in inventory.items():
        if quantity == 0:
            del inventory[item]
    return inventory

stock = {
    "apples": 5,
    "bananas": 0,
    "oranges": 3,
    "pears": 0,
}
print("Available stock:", remove_out_of_stock(stock))
