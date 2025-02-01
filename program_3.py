def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

    calculate_total_purchase()
item1 = input("enter item 1:")
price1 = float(12.99)
print (item1, '=', "$",price1)

item2 = input("enter item 2:")
price2 = float(22.99)
print (item2, '=', "$",price2)

item3 = input("enter item 3:")
price3 = float(17.99)
print (item3, '=', "$",price3)

item4 = input("enter item 4:")
price4 = float(2.99)
print (item4, '=', "$",price4)

item5 = input("enter item 5:")
price5 = float(9.99)
print (item5, '=', "$",price5)

subtotal = price1 + price2 + price3 + price4 + price5
print ("Subtotal =", subtotal)

tax = subtotal * 0.07
print ("Sales Tax = $",tax)

total = subtotal + tax
print ("Total Sale = $",total)