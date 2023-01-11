import random
import tkinter as tk

def update_values():
    global inventory, production_rate, demand, cost_per_unit, profit
    inventory_label.config(text=str(inventory))
    production_rate_label.config(text=str(production_rate))
    demand_label.config(text=str(demand))
    cost_per_unit_label.config(text=str(cost_per_unit))
    profit_label.config(text=str(profit))

def produce():
    global inventory, production_rate, demand, cost_per_unit, profit
    inventory += production_rate
    update_production_rate()
    update_values()

def sell():
    global inventory, production_rate, demand, cost_per_unit, profit
    sold = min(inventory, demand)
    inventory -= sold
    profit += sold * cost_per_unit
    update_demand()
    update_values()

def adjust_price():
    global inventory, production_rate, demand, cost_per_unit, profit
    new_price = int(price_entry.get())
    cost_per_unit = new_price
    update_values()

def update_demand():
    global demand
    demand = random.randint(5, 15)
    update_values()

def update_production_rate():
    global production_rate
    if inventory > 50:
        production_rate = 2
    elif inventory > 20:
        production_rate = 4
    else:
        production_rate = 6
    update_values()

# Set up the initial conditions of the game
inventory = 100
production_rate = 5
demand = 10
cost_per_unit = 1
profit = 0

# Create the main window
root = tk.Tk()
root.title("Supply Chain Game")

# Create labels to display the game values
inventory_label = tk.Label(root, text=str(inventory))
inventory_label.grid(row=0, column=1)
production_rate_label = tk.Label(root, text=str(production_rate))
production_rate_label.grid(row=1, column=1)
demand_label = tk.Label(root, text=str(demand))
demand_label.grid(row=2, column=1)
cost_per_unit_label = tk.Label(root, text=str(cost_per_unit))
cost_per_unit_label.grid(row=3, column=1)
profit_label = tk.Label(root, text=str(profit))
profit_label.grid(row=4, column=1)

# Create labels to display the game variables
tk.Label(root, text="Inventory:").grid(row=0, column=0)
tk.Label(root, text="Production Rate:").grid(row=1, column=0)
tk.Label(root, text="Demand:").grid(row=2, column=0)
tk.Label(root, text="Cost per Unit:").grid(row=3, column=0)
tk.Label(root, text="Profit:").grid(row=4, column=0)

# Create buttons for the player's actions
produce_button = tk.Button(root, text="Produce", command=produce)
produce_button.grid(row=5, column=0)
sell_button = tk.Button(root, text="Sell", command=sell)
sell_button.grid(row=5, column=1)

# Create an entry and a button for adjusting the price
price_entry = tk.Entry(root)
price_entry.grid(row=6, column=0)
adjust_price_button = tk.Button(root, text="Adjust Price", command=adjust_price)
adjust_price_button.grid(row=6, column=1)

# Start the main loop
root.mainloop()
