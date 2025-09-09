# pip install prettytable 
# MODULES  -> 1.PrettyTable     2.TextTable     3.BeautifulTable        4.Tabulate

from prettytable import PrettyTable



# create columns

table = PrettyTable(["Rollno","Name","Marks"])

# Add Rows

table.add_row([501,"Varma",89])
table.add_row([502,"Ganesh",92])
table.add_row([503,"Nikil",95])
table.add_row([508,"Nimesh",100])
table.add_row([510,"Naresh",93])


print(table)

output:
+--------+--------+-------+
| Rollno |  Name  | Marks |
+--------+--------+-------+
|  501   | Varma  |   89  |
|  502   | Ganesh |   92  |
|  503   | Nikil  |   95  |
|  508   | Nimesh |  100  |
|  510   | Naresh |   93  |
+--------+--------+-------+
