# name = input("Введите ваше имя: ")
# if name == "Urban":#  двойной знак == проверка на ревенство (Один знак = присвоение) # символ двоеточия (:) говорит об окончании формирования услоовия  и последующий код должен идти с 4 мя пробелами
#     print("Здравствуйте, администратор")
# else:  # <==  else ДВОЕТОЧИЕ,еще одна команда переводится как "иначе" и выполняется в случае не выполнения if
#     print("Привет", name)
# if name == "Валера": <== if (если)
#     print("Здравствуйте, студент")
#=======================================================================================================================
# number = int(input("Введите число: "))
# if number % 3 == 0 and number % 5 == 0:# or или and  не строгий и строгий оператор (or-либо) (and-и)
#  # elif если не требуется проверять следующее условие при выполнении первого и (самого сложного)
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else: # else - означает иначе, кроме или еще
#     print("Число не подходит")
#=======================================================================================================================
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first != second and second != third and first != third:
    print(0)
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)

