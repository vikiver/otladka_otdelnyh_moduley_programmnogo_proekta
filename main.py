import module1
import module2.py
import module3

print('Список создан...\n')

userList = [] 
while True:
     listElem = input('Введите элемент списка ')
     if listElem == '' or listElem == ' ':
          break
     else:
          userList.append(int(listElem))

print('\n1 - Вывести первый и последний элемент списка')
print('2 - Вывести сумму всех элементов')
     print('3 - вывести количество элементов')
     print('\nВыберите операцию, которую хотите выполнить. Для этого введите номер операции: ')
     option = int(input()

if option == 1:
     module1.first_and_last_ite(userList)
elif option == 2:
     module2.lis_sum(userList)
elif option == 4:
     module3.amount_of_all_items(userList)
