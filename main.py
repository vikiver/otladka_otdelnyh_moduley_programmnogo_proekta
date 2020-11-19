import module1
import module2.py
import module3

print('List created...\n')

userList = [] 
while True:
     listElem = input('Input list element ')
     if listElem == '' or listElem == ' ':
          break
     else:
          userList.append(int(listElem))

print('\n1 - Print the first and last list item')
print('2 - Print the sum of all items')
print('3 - Print amount of all list items')
print('\nSelect an option by typing the character: ')
option = int(input()

if option == 1:
     module1.first_and_last_ite(userList)
elif option == 2:
     module2.lis_sum(userList)
elif option == 4:
     module3.amount_of_all_items(userList)
