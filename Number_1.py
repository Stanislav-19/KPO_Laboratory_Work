a = int(input())
b = int(input())
c = int(input())
if a>=1 and c<=10:
    result_1 = int(a+b*c)
    result_2 = int(a*b+c)
    result_3 = int(a*b*c)
    result_4 = int((a+b)*c)
    result_5 = int(a + b + c)
    result_6 = int(a * (b + c))
    list = [result_1,result_2,result_3,result_4,result_5,result_6]
    list.sort()
    print (int(list[-1]))
else:
    print('Вы ввели неверное значение')
