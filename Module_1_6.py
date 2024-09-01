#Практическое задание по теме: "Словари и множества"

my_dict = {'Сергей':1986,'Наташа':1993, "Виктория":2013}
print(my_dict)
print(f"Существующее значение: ",(my_dict.get("Наташа")))
print(f"Не существующее значение: ",(my_dict.get("Галина")))
my_dict.update({"Татьяна":2009,
                "Надежда":1989})
a = my_dict.pop("Надежда")
print(f"Удалённый: ", a)
print(f'Обновлённый список:',my_dict)

my_set = {11,11, "Арбуз","Арбуз", "Ягода","шмягода)",3.14,False,}
print(my_set)
my_set.add((25,52,52,25))
my_set.add(True)
print(my_set.remove(False))
print(f'Обновлённый my_set: ', my_set)