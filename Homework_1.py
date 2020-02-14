# 1.1является ли строка записью числа
row=input("Please enter string value:")
print("Is the row above is a number?:", row.isdigit());

# 1.2сколько пробелов в строке
row1=input("Please enter the string value with the spaces:")
sub=" "
print("How many spaces do we have in the row above?:", row1.count(sub,0,len(row1)))

# 1.3сколько символов точки у вас в строке
row2=input("Please enter some free text with dot's:")
sub="."
print("How many dot's do we have in the row above?:",row2.count(sub,0,len(row2)))

# 1.4 строка Homework. Преобразовать строку в длину 100 символов.По средине которой исходное слово, а с обоих сторон -
# пробелы
row3=input("Please enter word 'Homework':")
print("Move word to the center:", row3.center(100," "))

# 1.5 сделайте первые буквы слов строки большие
row4=input("Please enter free text:")
print("First word from uppercase:",row4.capitalize())


#2.1 вычислить длину гипотенузы со сторонами 158 и 971
a=float(158)
b=float(971)
print("Длина гипотенузы:", round((a*a +b*b)**0.5));

#2.2 дано двухзначное число. Найдите число десятков в нем.
numb=input("Введите двухзначное число:")
print(numb[0]);

#2.3 дано трехзначеное число. Найдите сумму его цифр
n = input("Введите трехзначное число:")
mult = 1
summa = 0
for i in n:
    summa += int(i)
    if int(i) != 0:
        mult *= int(i)
print("Сумма цифр:", summa)

#2.4 вывести следующее парное число
z=int (input("Введите целое число:"))
x=int(z+1)%2
if x==0:
    print("Следующее парное число:", z+1)
else:
    print("Следующее парное число:", z+2)

#2.5 вывести дробную часть числа
y=float(input("Положительное действительное число Х:"))
print("Дробная часть:", y-int(y))

#2.6 вывести первое число после запятой
z3=float(input("Положительное действительное число Х1:"))
z4 = int(z3*10)%10
print("Первое число после запятой:", z4)

#3
year=int(input("Year:"))
t=year%4
t1=year%100
t2=year%400
if (t==0 and t1!=0) or t2==0:
    print("Высокосный год-YES")
else:
    print("Не высокосный год-NO")

#4
a=int(input("Введите сторну а="))
b=int(input("Введите сторну b="))
c=int(input("Введите сторну c="))
if a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")

#5
try:
    a = int(input("input first number: "))
except:
    a = int(input("please input int for first number: "))
b = int(input("input second number: "))
c = int(input("input third number: "))
l = [a, b, c]
l.sort()
print(l)

#6
a = int(input("Please input int number1: "))
b = int(input("Please input int number2: "))
c = int(input("Please input int number3: "))
if a == b == c :
    print(3)
elif a == b or a== c or b == c:
    print(2)
else:
    print(0)