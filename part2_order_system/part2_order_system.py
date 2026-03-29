# =========================================
# BitSom BA Assignment 3 — Part 2
# Restaurant Order Management System
# =========================================


# -------------------------------
# GIVEN DATA
# -------------------------------

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}


# =========================================
# TASK 1 — MENU DISPLAY
# =========================================

print("\n===== Restaurant Menu =====")

categories = []

for item in menu:
    cat = menu[item]["category"]
    if cat not in categories:
        categories.append(cat)

for cat in categories:
    print(f"\n===== {cat} =====")
    for item, details in menu.items():
        if details["category"] == cat:
            price = details["price"]
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item:<18} ₹{price:>7.2f}   [{status}]")

# ---- Summary ----
print("\n~~~~ Menu Summary ~~~~")

print("Total items on menu:", len(menu))

available_count = 0
for d in menu.values():
    if d["available"]:
        available_count += 1
print("Available items:", available_count)

max_price = 0
max_item = ""
for item, d in menu.items():
    if d["price"] > max_price:
        max_price = d["price"]
        max_item = item

print(f"Most expensive item: {max_item} (₹{max_price})")

print("\nItems under ₹150:")
for item, d in menu.items():
    if d["price"] < 150:
        print(f"{item:<15} ₹{d['price']:.2f}")


# =========================================
# TASK 2 — CART OPERATIONS
# =========================================

cart = []

def add_item(name, qty):
    if name not in menu:
        print("Item not found:", name)
        return
    if not menu[name]["available"]:
        print("Item unavailable:", name)
        return

    for it in cart:
        if it["item"] == name:
            it["quantity"] += qty
            return

    cart.append({"item": name, "quantity": qty, "price": menu[name]["price"]})

def remove_item(name):
    for it in cart:
        if it["item"] == name:
            cart.remove(it)
            return
    print("Item not in cart:", name)

def show_cart():
    print("\nCart State:")
    for it in cart:
        print(it)

# Simulation
add_item("Paneer Tikka", 2)
show_cart()

add_item("Gulab Jamun", 1)
show_cart()

add_item("Paneer Tikka", 1)
show_cart()

add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)

remove_item("Gulab Jamun")
show_cart()

# ---- Order Summary ----
print("\n========== Order Summary ==========")

subtotal = 0
for it in cart:
    total = it["quantity"] * it["price"]
    subtotal += total
    print(f"{it['item']:<18} x{it['quantity']}    ₹{total:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total_pay = subtotal + gst

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):               ₹{gst:.2f}")
print(f"Total Payable:          ₹{total_pay:.2f}")
print("====================================")


# =========================================
# TASK 3 — INVENTORY + DEEP COPY
# =========================================

import copy

inventory_backup = copy.deepcopy(inventory)

print("\n--- Deep Copy Check ---")

inventory["Paneer Tikka"]["stock"] = 5
print("Modified:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

# restore
inventory["Paneer Tikka"]["stock"] = inventory_backup["Paneer Tikka"]["stock"]

# Deduct stock
print("\n--- Updating Inventory ---")

for it in cart:
    name = it["item"]
    qty = it["quantity"]

    if inventory[name]["stock"] >= qty:
        inventory[name]["stock"] -= qty
    else:
        print("⚠ Not enough stock for", name)
        inventory[name]["stock"] = 0

# Alerts
print("\n--- Reorder Alerts ---")

for item, d in inventory.items():
    if d["stock"] <= d["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {d['stock']} unit(s) left (reorder level: {d['reorder_level']})")

print("\n--- Final Inventory Check ---")
print("Current:", inventory)
print("Backup:", inventory_backup)


# =========================================
# TASK 4 — SALES ANALYSIS
# =========================================

print("\n--- Daily Revenue ---")

revenue = {}

for date, orders in sales_log.items():
    total = 0
    for o in orders:
        total += o["total"]
    revenue[date] = total
    print(f"{date} : ₹{total}")

best_day = max(revenue, key=revenue.get)
print("Best Selling Day:", best_day)

# Most ordered item
count = {}

for orders in sales_log.values():
    for o in orders:
        for item in o["items"]:
            count[item] = count.get(item, 0) + 1

print("Most Ordered Item:", max(count, key=count.get))

# Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\n--- Updated Revenue ---")

revenue = {}
for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    revenue[date] = total
    print(f"{date} : ₹{total}")

print("Updated Best Day:", max(revenue, key=revenue.get))

# Enumerate orders
print("\n--- All Orders ---")

i = 1
for date, orders in sales_log.items():
    for o in orders:
        items_str = ", ".join(o["items"])
        print(f"{i}. [{date}] Order #{o['order_id']} — ₹{o['total']:.2f} — Items: {items_str}")
        i += 1