cart=[]

while True:
    print("\n 1) Add Item  2) View Items  3) Delete Item  4) Exit")
    choice = input("Choose options: ")
    if choice == "1":
        item = input("Enter an item: ").strip()
        price = float(input("Enter item price: "))
        cart.append({"item": item, "Price": price})
        print(f"Added Item: {item} (${price})")
    elif choice == "2":
        if not cart:
            print("Cart is empty.")
        else:
            for i, it in enumerate(cart, start=1):
                print(f"{i}. {it['item']} - ${it['Price']:.2f}")
    elif choice == "3":
        item_to_delete = input("Enter item name to delete: ").strip()
        for i, it in enumerate(cart):
            if it["item"].lower() == item_to_delete.lower():
                removed = cart.pop(i)
                print(f"{removed['item']} removed from the cart.")
                break
        else:
            print(f"{item_to_delete} is not in the cart.")
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

