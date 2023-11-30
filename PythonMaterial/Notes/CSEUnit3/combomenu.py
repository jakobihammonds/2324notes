# Start of Iteration 1

print("McJonalds Ordering System")
total = 0.00
size = "none"
ordercont = []
frize = "none"
mega = "none"
order = ""
sandwich = input("What kind of sandwich do you want, we have Chicken, Beef, and Tofu, or none.\n")

while sandwich != 'none':
  if sandwich == 'Chicken' or sandwich == 'chicken' :
    total += 5.25
    ordercont.append("Chicken Sandwich")
    sandwich = input("Would you like another sandwich? (Chicken, Beef, and Tofu, or none\n")
  elif sandwich == 'Beef' or sandwich == 'beef' :
    total += 6.25
    order = "Beef Sandwich"
    ordercont.append("Beef Sandwich")
    sandwich = input("Would you like another sandwich? (Chicken, Beef, and Tofu, or none\n")
  elif sandwich == 'Tofu' or sandwich == 'tofu' :
    total += 5.75
    order = "Tofu Sandwich"
    ordercont.append("Tofu Sandwich")
    sandwich = input("Would you like another sandwich? (Chicken, Beef, and Tofu, or none\n")
  
  else:
    print("That's not an option")
    sandwich = input("Would you like a sandwich? Chicken, Beef, and Tofu, or none\n")

  
  
    # Start of Iteration 2 
drink = input("What size of drink do you want, Small, Medium, Large, or none\n")
while drink != 'none':
  if drink == 'Small' or drink == 'small' :
    total += 1.00
    ordercont.append("Small Drink")
    drink = input("Would you like another drink? (Small, Medium, Large, or none\n")
  elif drink == 'Medium' or drink == 'medium' :
    total += 1.75
    ordercont.append("Medium Drink")
    drink = input("Would you like another drink? (Small, Medium, Large, or none\n")
  elif drink == 'Large' or drink == 'large' :
    child = input("Would you like to child-size your drink for only .38 cents more?\n")
    if child == 'No' or child == 'no' :
      total += 2.25
      ordercont.append("Large Drink")
    if child == 'Yes' or child == 'yes' :
      total += 2.25+.38
      ordercont.append("Child-Sized Drink")
    drink = input("Would you like another drink? (Small, Medium, Large, or none\n")

  else:
    print("That's not an option")
    drink = input("Would you like a drink (Small, Medium, Large, or none\n")
        
    # Start of Iteration 3
frize = input("Would you like some fries? (Small, Medium, Large, or none\n")
while frize != 'none':
  if frize == 'Small' or frize == 'small' :
    total += 1.00
    ordercont.append("Small Fries")
    frize = input("Would you like some more fries? (Small, Medium, Large, or none\n")
  elif frize == 'Medium' or frize == 'medium' :
    total += 1.50
    ordercont.append("Medium Fries")
    frize = input("Would you like some more fries? (Small, Medium, Large, or none\n")
  elif frize == 'Large' or frize == 'large' :
    mega = input("Would you like to mega size your fries?\n")
    if mega == 'Yes' or mega == 'yes' :
      total += 2.50
      ordercont.append("Mega Fries")
      frize = input("Would you like some more fries? (Small, Medium, Large, or none\n")
    elif mega =='No' or mega == 'no' :
      total += 2.00
      ordercont.append("Large Fries")
      frize = input("Would you like some more fries? (Small, Medium, Large, or none\n")

  else:
    print("That's not an option")
    frize = input("Would you like some fries? (Small, Medium, Large, or none\n")

# Iteration 4
# urmoms

ketchup_packet = input("Do you want ketchup?\n")
packetamount = 0.00

if ketchup_packet == 'Yes' or ketchup_packet == 'yes' :
  packets = input("How many packets?\n")
  packetamount = 0.25*int(packets)
  total += packetamount
  ordercont.append(packets + " Ketchups Packets")
if ketchup_packet == 'No' or ketchup_packet == 'no' : 
  total += 0.00
  ordercont.append("No Ketchup")
  

 
# Iteration FIVE
      
print("\nFood Ordered:")
for ordercont in ordercont:
  print(ordercont)
# End of Ketchup
      
print("\nTotal Cost ")
if sandwich == 'Chicken' or sandwich == 'chicken' or sandwich == 'Beef' or sandwich == 'beef' or sandwich == 'Tofu' or sandwich == 'tofu' and drink == 'yes'  or drink == 'Yes' and frize == 'yes' or frize == 'Yes' :
  total = total - 1.00
tax = round(total*.07, 2)
total = round(total, 2)
totaltotal = tax+total
print("Subtotal: $" + str(total))
print("Tax: $" + str(tax))
charity = input("Would you like to round up for the Jonald McRonald foundation.\n")
if charity == 'Yes' or charity == 'yes' : 
  print("Total: $" + "%.2f" % round(totaltotal))
if charity == 'No' or charity == 'no' :
  print("Total: $" + "%.2f" % totaltotal)
      
