from datetime import datetime
print("------------------------Welcome----------------------------")
name=input("Enter your name:")

# lists of items
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/kg
Paneer  Rs 110/kg
Maggi   Rs 20/kg
Boost   Rs 90/each
Colgate Rs 75/each
'''

# declaration
price=0
pricelist=[]
toralproce=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,
       'sugar':30,
       'salt':20,
       'oil':80,
       'panner':110,
       'maggi':20,
       'boost':90,
       'colgate':75}
option = int (input("For list of items press 1:"))
if option==1:
    print(lists)