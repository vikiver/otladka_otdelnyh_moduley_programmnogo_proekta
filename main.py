import module1
import module2
import module3
import module4
import module5

print('Список создан...\n')

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
print('4 - ')
print('5 - вывести все нечётные элементы')
print('\nВыберите операцию, которую хотите выполнить. Для этого введите номер операции: ')
option = int(input())

if option == 1:
     module1.first_and_last_items(userList)
elif option == 2:
     module2.lis_sum(userList)
elif option == 3:
     module3.amount_of_all_items(userList)
elif option == 4:
     module4.even_items(userList)
elif option == 5:
     module5.odd_items(userList)
