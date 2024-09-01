#Практическая работа по уроку: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = 1,2,'a','b'
print(immutable_var)
#immutable_var[2] = "c" #TypeError: 'tuple' object does not support item assignment (TypeError: объект 'tuple' не поддерживает присвоение элементов)
#print(immutable_var)
mutable_list =[1,2,"a","b",]
mutable_list.append("Modified")
print(mutable_list)