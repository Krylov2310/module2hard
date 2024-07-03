task = 'Дополнительное практическое задание по модулю*(Задание "Слишком древний шифр":)'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
# Запрограмированные группы паролей
real_pass = [[3,12], [4,13], [5,1423], [6,121524], [7,162534], [8,13172635], [9,1218273645], [10,141923283746],
    [11,11029384756], [12,12131511124210394857], [13,112211310495867], [14,1611325212343114105968],
    [15,1214114232133124115106978], [16,1317115262143531341251161079], [17,11621531441351261171089],
    [18,12151811724272163631545414513612711810], [19,118217316415514613712811910], [20,13141911923282183731746416515614713812911]]
#print(real_pass)
check = len(real_pass)
#print(check, type(check))
# Алгоритм расчета пароля от введенного числа
def gen_passwords(n):
    result = ""
    numb = (n + 1) // 2
    for i in range(1, numb):
        j = i + 1
        while i + j <= n:
            f = n % (i + j)
            if f == 0:
                result += str(i) + str(j)
            j = j + 1
    return result

# Ввод числа пользователем
num = 0
while num < 3 or num > 20:
    print('Вы в западне и что бы выбраться из нее Вам предстоит сгенерировать пароль')
    num = int(input("Введите число для генерации пароля в диапазоне от 3 до 20: "))
password = gen_passwords(num)

# Сверка запрограмированного пароля со сгенерированным
check2 = 0
for r in real_pass:
    pass1 = [num, int(password)]
    check2 = check2 + 1
    if r == pass1:
        print(f'Исходный сгенерированный пароль: {r}')
        print(f"Ваш пароль: {num} - {password}")
        print("Мои поздравления, вы выбрались из ловушки :-)")
        break
    if r != pass1 and check == check2:
        print('К великому сожелению ваш пароль не подошел и вы погибли :-(')
        continue
print()
print(thanks)