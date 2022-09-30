year = 2020

book1 = 100
book2 = 200
book3 = 300

value_de = 0.9 # Value decrease 10% per year.

result = book1 * value_de
newresult = result * value_de
    
current_price = 100
år = 2022
inköpsår = 2020

# Om en bok är inköpt 2022 så är den värd 100%. 
if inköpsår == år:
    print(current_price)
elif inköpsår < år: # För varje år det gått så ska den minska 10%.
    årskillnad = år - inköpsår # = 2 i detta läge.
    ettårvärde = current_price * value_de # Värde efter ett år
    
    print(ettårvärde * value_de)
      
mylist = [100, 200]

