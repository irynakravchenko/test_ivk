#1
s=input("Введите строку:")
print('3 символ:', s[2])
print('предпоследний символ:', s[-2])
print('первые пять символов', s[0:5])
print('кроме двух последних:', s[:-2])
print('символы c четным индексом:', s[0::2])
print('символы c нечетным индексом:', s[1::2])
print('символы в ообратном порядке:', s[::-1])
print('символы в ообратном порядке через один:', s[::-2])
print('символы в ообратном порядке через один начиная с предпоследнего:', s[-2::-2])
print('символы в ообратном порядке без первого и предпоследнего:', s[1:-1:1])
print("длина всей строки:", len(s))

#2
s2 = input("Ввведите строку: ")
l = len(s2)
l1 = len(s2)+1
if len(s2)%2 == 0:
    print("2 половины если строка четная:", s2[0:l//2],s2[l//2:])
elif len(s2)%2 !=0:
    print("2 половины если строка нечетная+1, поменянные местами:",s2[l//2:],s2[0:l1//2])

#3
count = 0
while (count < 11):
   print ('От 0 до 10:', count)
   count = count + 1


#3
i = 1
while (i < 22):
   print ('От 1 о 21:', i)
   i = i + 1

#4
#1
l=[10,20,32,56,23]
while l:
  print(l.pop(0))

