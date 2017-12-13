# CTI-110 
# M2HW2 - Tip Tax Total 
# Juan Santiago
# 9/15/2017

foodPrice = float( input( "Please enter the charge of the food: " ) )
tip = 0.18 * foodPrice
salesTax = 0.07 * foodPrice
total = foodPrice + tip + salesTax

print( "Charge: $" + format( foodPrice, ",.2f"), "Tip: $" + \
       format ( tip, ",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
       "Total: $" + format( total, ",.2f"), sep = "\n" )
