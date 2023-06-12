items_dict = {}


def remove(name, count, stock):
    if name in stock.keys():
        if stock[name] < count:
            print(f"Not enough quantity, we only have {stock[name]} {name}.")
        else:
            stock[name] -= count
            print(f"You have removed {count} {name}.")
    else:
        print(f"Sorry, we do not have any {name}.")


def load(name, count, stock):
    if name not in stock.keys():
        stock[name] = count
    else:
        stock[name] += count
    print(f"You have restocked {count} {name}.")


def audit(stock):
    print("Current stock in warehouse:")
    for key, value in stock.items():
        print(f"{key} {value}")


while True:
    command = input("Please, enter the action(load/remove/audit/exit): ")
    if command == "exit":
        break
    if command == "audit":
        audit(items_dict)
        continue
    item_name = input("Which item would you like to load/remove: ")
    item_count = int(input("How many: "))

    if item_count <= 0:
        print("Invalid input! You can only enter positive values!")
        continue

    if command == "remove":
        remove(item_name, item_count, items_dict)
    elif command == "load":
        load(item_name, item_count, items_dict)

audit(items_dict)

