import module1.py
import module2.py
import module3.py
import module4.py
import module5.py

print('Список создан...\n')

userList = [] 
while True:
     listElem = int(input('Введите элемент списка. Введите пробел, если хотите закончить создание списка '))
     if listElem == '' or listElem == ' ':
          break
     else:
          userList.append(listElem)

print('\n1 - Вывести первый и последний элемент списка')
print('2 - Вывести сумму всех элементов')
print('3 - вывести количество элементов')
print('4 - вывести все чётные элементы')
print('5 - вывести все нечётные элементы')
print('\nВыберите операцию, которую хотите выполнить. Для этого введите номер операции: ')
option = int(input()

if option == 1:
     module1.first_and_last_items(userList)
elif option == 2:
     module2.lis_sum(userList)
elif option == 3:
     module3.amount_of_all_items(userList)
elif option == 4:
     module3.even_items(userList)
elif option == 5:
     module3.odd_items(userList)
