# Module 6: Portfolio Milestone
# Step 4 - Build the ShoppingCart class with the following data attributes and related methods.
def main():
    # Parameterized constructor, which takes the customer name and date as parameters
    # name initialized to none, date to January 1, 2020
    class ShoppingCart:
        def __init__(self, customer_name = None, current_date = 'January 1, 2020'):
            self.customer_name = customer_name
            self.current_date = current_date
            self.cart_items = []

        # Method - Add Item
        def add_item(self, itemName):
            self.cart_items.append(itemName)

        # Method - Remove Item
        def remove_item(self, itemName):
            found = False
            for item in self.cart_items:
                if item['itemName'] == itemName:
                    self.cart_items.remove(item)
                    found = True
            if not found:
                print('Item not found in cart. Nothing removed.')

        # Method - Modify Item
        def modify_item(self, itemName, price = None, quantity = None, description = None):
            found = False
            for item in self.cart_items:
                if item['itemName'] == itemName:
                    if description is not None:
                        item['description'] = description
                    if quantity is not None:
                        item['quantity'] = int(quantity)
                    if price is not None:
                        item['price'] = float(price)
                    found = True
            if not found:
                print('Item not found in cart. Nothing modified.')

        # Method - Get the Number of Items in Cart
        def get_num_items_in_cart(self):
            total_quantity = sum([item['quantity'] for item in self.cart_items])
            return total_quantity

        # Method - Get the Total Cost of the Cart
        def get_cost_of_cart(self):
            cart_cost = round(sum(item['price'] * item['quantity'] for item in self.cart_items),2)
            return cart_cost

        # Method - Print the Total Cost of the Cart
        def print_total(self):
            if not self.cart_items:
                print('SHOPPING CART IS EMPTY')
            else:
                print(self.customer_name + "'s Shopping Cart - " + self.current_date)
                print('Number of Items: ' + str(self.get_num_items_in_cart()))
                # Print the description, quantity, and price, and total for just that item
                for item in self.cart_items:
                    print(item['itemName'] + ' ' + str(item['quantity']) + ' @ $' + str(item['price']) + ' = $' + str(round(item['quantity'] * item['price'],2)))
                # Print the total for all items in cart
                print('Total: $' + str(self.get_cost_of_cart()))

        # Method - Print the descriptions for All Items in the Cart
        def print_description(self):
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print('Item Descriptions')
            for Item in self.cart_items:
                print(Item['itemName'] + ' - ' + Item['description'])

# Step 5 - In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single character. Build and output the menu within the function. If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before implementing other options. Call print_menu() in the main() function. Continue to execute the menu until the user enters q to Quit
# Print the shopping cart options menu
    def print_menu(cart):
        option = ''
        while option != 'q':
            print('MENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item')
            print('d - Output item descriptions')
            print('o - Output shopping cart')
            print('q - Quit')
            option = input('Choose an option: ')
            # Add Item
            if option == 'a':
                itemName = input('Enter item name: ')
                description = input('Enter the item description: ')
                price = float(input('Enter the item price: '))
                quantity = int(input('Enter the item quantity: '))
                ItemToPurchase = {'itemName': itemName, 'description': description, 'price': price, 'quantity': quantity}
                cart.add_item(ItemToPurchase)
            # Remove Item
            elif option == 'r':
                itemName = input('Enter the name of the item to remove: ')
                cart.remove_item(itemName)
            # Modify Item
            elif option == 'c':
                itemName = input('Enter the name of the item to modify: ')
                whatToChange = input('What would you like to modify? description, quantity, or price? ')
                # Modify Description
                if whatToChange  == 'description':
                    newDescription = input('Enter the new description: ')
                    cart.modify_item(itemName, description = newDescription)
                # Modify Quantity
                elif whatToChange  == 'quantity':
                    newQuantity = int(input('Enter the new quantity: '))
                    cart.modify_item(itemName, quantity = newQuantity)
                # Modify Price
                elif whatToChange  == 'price':
                    newPrice = float(input('Enter the new price: '))
                    cart.modify_item(itemName, price = newPrice)
            # Print Description
            elif option == 'd':
                cart.print_description()
            # Print Total
            elif option == 'o':
                cart.print_total()
            # Quit
            elif option == 'q':
                return
            # Invalid Input
            else:
                print('Invalid input. Please try again.')

# Step 6 - Implement Output shopping cart menu option. Implement Output item's description menu option.
    # Implement Output Shopping cart menu option and item's description menu option
    customer_name = input('Enter the customer name: ')
    current_date = input('Enter the current date: ')
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)
main()