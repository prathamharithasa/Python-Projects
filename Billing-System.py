import datetime

cart = []  # List to store items added by user
GST_RATE = 0.09  # GST 9%

def input_customer_info():
    print("=== Customer Information ===")
    name = input("Enter customer name: ").strip()
    while True:
        phone = input("Enter phone number (8 digits): ").strip()
        # Check if phone number has exactly 8 digits
        if phone.isdigit() and len(phone) == 8:
            break
        print("Invalid phone number. Please enter exactly 8 digits.")
    return name, phone  # Return customer info

def add_item():
    while True:
        name = input("Enter item name: ").strip()
        if not name:
            print("Item name cannot be empty.")  # Validate item name input
            continue
        try:
            price = float(input(f"Enter price of {name}: $"))
            if price <= 0:
                print("Price must be greater than zero.")
                continue
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {name}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            continue

        # Add the item to the cart as a dictionary
        cart.append({"name": name, "price": price, "quantity": quantity})
        print(f"Added {quantity} x {name} at ${price:.2f} each.")
        break

def remove_item():
    if not cart:
        print("Cart is empty, nothing to remove.")
        return
    print("\nItems in Cart:")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} x {item['quantity']}")

    while True:
        try:
            choice = int(input("Enter item number to remove (or 0 to cancel): "))
            if choice == 0:
                print("No items removed.")
                break
            # Remove the selected item from cart list
            if 1 <= choice <= len(cart):
                removed = cart.pop(choice - 1)
                print(f"Removed {removed['name']} from the cart.")
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_subtotal():
    # Calculate total price before tax
    return sum(item["price"] * item["quantity"] for item in cart)

def calculate_gst(subtotal):
    # Calculate GST amount
    return subtotal * GST_RATE

def print_receipt(customer_name, customer_phone):
    if not cart:
        print("Cart is empty. No receipt to print.")
        return

    print("\n======= SUPERMARKET RECEIPT =======")
    print(f"Customer: {customer_name}")
    print(f"Phone: {customer_phone}")
    print("Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\nItem            Qty  Price   Total")
    print("--------------------------------------")

    # Print each item with quantity and price
    for item in cart:
        total = item["price"] * item["quantity"]
        print(f"{item['name']:<15} {item['quantity']:<3}  ${item['price']:<6.2f} ${total:.2f}")

    subtotal = calculate_subtotal()  # Calculate subtotal
    gst = calculate_gst(subtotal)    # Calculate GST
    grand_total = subtotal + gst     # Final total with GST

    print("--------------------------------------")
    print(f"{'Subtotal':<25} ${subtotal:.2f}")
    print(f"{'GST (9%)':<25} ${gst:.2f}")
    print(f"{'Grand Total':<25} ${grand_total:.2f}")
    print("======================================")

    save = input("Save receipt to file? (yes/no): ").strip().lower()
    if save == 'yes':
        filename = f"receipt_{customer_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        # Write receipt details to a text file
        with open(filename, 'w') as f:
            f.write(f"Customer: {customer_name}\n")
            f.write(f"Phone: {customer_phone}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("Item            Qty  Price   Total\n")
            f.write("--------------------------------------\n")
            for item in cart:
                total = item["price"] * item["quantity"]
                f.write(f"{item['name']:<15} {item['quantity']:<3}  ${item['price']:<6.2f} ${total:.2f}\n")
            f.write("--------------------------------------\n")
            f.write(f"{'Subtotal':<25} ${subtotal:.2f}\n")
            f.write(f"{'GST (9%)':<25} ${gst:.2f}\n")
            f.write(f"{'Grand Total':<25} ${grand_total:.2f}\n")
        print(f"Receipt saved as '{filename}'")

def main():
    print("Welcome to the Advanced Supermarket Billing System")
    customer_name, customer_phone = input_customer_info()  # Get customer details

    while True:
        print("\nChoose an option:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            add_item()  # Add new item to cart
        elif choice == "2":
            remove_item()  # Remove item from cart
        elif choice == "3":
            if cart:
                print("\nCurrent Cart:")
                for i, item in enumerate(cart, 1):
                    print(f"{i}. {item['name']} x {item['quantity']} @ ${item['price']:.2f}")
            else:
                print("Cart is empty.")
        elif choice == "4":
            if cart:
                print_receipt(customer_name, customer_phone)  # Print and save receipt
            else:
                print("Cart is empty. Cannot checkout.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
