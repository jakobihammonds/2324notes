class Order:


  
  def __init__(self):
      self.items = []

  
  @staticmethod
  def check_user_input(user_items, menu):
        return all(item in menu for item in user_items)
  
  def set_items(self, items):
      self.items = items

  def add_item(self, item):
      self.items.append(item)

  def remove_item(self, item):
      if item in self.items:
          self.items.remove(item)
      else:
          print("Item not found in the order.")

  def clear_order(self):
      self.items = []

  def calculate_subtotal(self, menu):
      subtotal = sum(menu[item]['price'] for item in self.items)
      return subtotal

  
  def apply_discount(self):
      discountItems = {"1","10","20"}
      if all(item in self.items for item in discountItems):
          return 0.1  
        # this adds the 10% discount, dom helped me with the list function because my line was too long, if all items in selfitems are in discountitems then return 0.1
      return 0

def print_menu(menu):
  for key, value in menu.items():
      print(f"{key}. {value['name']} - ${value['price']:.2f}")

def print_order(order, order_number, menu):
  print(f"Order{order_number}:")
  for item in order.items:
      print(f"    {menu[item]['name']}")
  subtotal = order.calculate_subtotal(menu)
  discount = order.apply_discount()
  discount_amount = subtotal * discount
  discounted_subtotal = subtotal - discount_amount
  print(f"    Subtotal: ${discounted_subtotal:.2f}")
  return discounted_subtotal

#dom helped me with the menu and orders
def main():
  menu = {
      '1': {'name': 'Krabby Patty', 'price': 1.20},
      '2': {'name': 'Krabby Patty w/ Sea Cheese', 'price': 1.50},
      '3': {'name': 'Double Krabby Patty', 'price': 2.00},
      '4': {'name': 'Double Krabby Patty w/ Sea Cheese', 'price': 2.25},
      '5': {'name': 'Triple Krabby Patty ', 'price': 3.00},
      '6': {'name': 'Triple Krabby Patty w/ Sea Cheese', 'price': 3.25},
      '7': {'name': 'Small Coral Bits','price': 1.00},
      '8':  {'name': 'Medium Coral Bits','price': 1.25},
      '9': {'name': 'Large Coral Bits','price': 1.50},
      '10': {'name': 'Kelp Rings','price': 1.50},
      '11': {'name': 'Salty Sauce','price': 0.50},
      '12':  {'name': 'Krabby Meal','price': 3.50},
      '13': {'name': 'Double Krabby Meal','price': 3.75},
      '14': {'name': 'Triple Krabby Meal','price': 4.00},
      '15': {'name': 'Salty Sea Dog','price': 1.25},
      '16':  {'name': 'Footlong','price': 2.00},
      '17':  {'name': 'Sailors Surprise','price': 3.00},
      '18':  {'name': 'Golden Loaf','price': 2.00},
      '19':  {'name': 'Golden Loaf w/ Sauce','price': 2.50},
      '20':  {'name': 'Kelp Shake','price': 2.00},
      '21':  {'name': 'Small Seafoam Soda','price': 1.00},
      '22':  {'name': 'Medium Seafoam Soda','price': 1.25},
      '23':  {'name': 'Large Seafoam Soda','price': 1.50},







  }   

  orders = []
  order_number = 1

  while True:
      print("\nWelcome to the Krusty Krab!")
      print_menu(menu)

      user_input = input("\nEnter the menu numbers for your order (comma-separated): ")
      user_items = user_input.split(',')

      #make sure user input is good
      valid_input = Order.check_user_input(user_items, menu)
      while not valid_input:
          user_input = input("Invalid input. Please enter valid menu numbers: ")
          user_items = user_input.split(',')
          valid_input = Order.check_user_input(user_items, menu)

      # Create and add order
      order = Order()
      order.set_items(user_items)
      orders.append(order)

      # Print the order details
      order_total = print_order(order, order_number, menu)

      # Allow user to edit or delete order
      edit_choice = input("Do you want to edit or delete this order? (yes/no): ").lower()
      if edit_choice == 'yes':
          while True:
              edit_option = input("Enter 'add', 'remove', or 'delete': ").lower()
              if edit_option == 'add':
                  additional_items = input("Enter additional menu numbers to add (comma-separated): ").split(',')
                  valid_input = Order.check_user_input(additional_items, menu)
                  while not valid_input:
                      additional_items = input("Bad input. Please enter valid menu numbers: ").split(',')
                      orders.__add__(additional_items)
                  order.add_item(additional_items)
              elif edit_option == 'remove':
                  item_to_remove = input("Enter menu number to remove: ")
                  order.remove_item(item_to_remove)
              elif edit_option == 'delete':
                  orders.remove(order)
                  print(f"Order {order_number} deleted.")
                  break
              else:
                  print("Not an option. Please enter 'add', 'remove', or 'delete'.")

              # Print updated order details
              order_total = print_order(order, order_number, menu)

      order_number += 1

      # Ask if the user wants to place another order
      another_order = input("Do you want to place another order? (yes/no): ").lower()
      if another_order != 'yes':
          break

  print("\nThank you for coming to the Krusty Krab!")
  print("\nOrder Summary:")
  total_amount = 0
  for i, order in enumerate(orders, start=1):
      total_amount += print_order(order, i, menu)

  tax_amount = total_amount * 0.07
  final_amount = total_amount + tax_amount

  print(f"\nTax Amount: ${tax_amount:.2f}")
  print(f"Final Amount: ${final_amount:.2f}")

if __name__ == "__main__":
  main()