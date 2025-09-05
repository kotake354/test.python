#pythonの文法～制御構文

#if文(true)
a = 1
if a > 0:
    print('plus')
#if文(false)
a = 0
if a > 0:
    print(plus)

#比較演算子
#A==B   AとBが等しいければture
#A!=B   AとBが等しくなければture
#A<B    AがBよりも小さければture
#A>B    AがBよりも大きければture
#A<=B   AがB以下ならture
#A>=B   AがB以上ならture

print(123*456 <= 50000)
print(12345678 % 9 == 0)

#ブール演算子
#A and B    AかつB（AとBがtureの時ture、それ以外はfalse)
#A or B     AまたはB（AとBがfalseの時false、それ以外はture)
#not A      Aではない（Aがtureの時false、Aがfalseのときture)
print(12 < 34 and 56 < 78)
print(12 < 34 and 56 > 78)

print(21 < 34 or 65 > 78)
print(21 > 34 or 65 > 78)

print(not 12 < 34)
print(not 12 > 34)

#else節
#if     式：    tureの時処理
#else   式：    elseの時処理
a = 1
if a < 0:
    print('plus')
else:
    print('not plus')

#elif節
#if     式A：   式Aがtureの時処理
#elif   式B:    式Aがfalseで、式Bがtureの時の処理
#else   式Aも式Bもfalseの時の処理
a = 0
if a > 0:
    print('plus')
elif a < 0:
    print('minus')
else :
    print('zero')

#for文
number = ['one' , 'two' , 'three']
for n in number:
    print(n)

#range関数
for x in range(10):
    print(x)
for x in range (5):
    print(x, end='')
for x in range(10,21):
    print(x,end='')
for x in range(20,31,2):
    print(x, end='')

#enumerate関数
fruit = ['apple' , 'banana', 'coconut']
for i, x in enumerate(fruit):
    print(i, x)

fruit = ['apple' , 'banana', 'coconut']
for i, x in enumerate(fruit, 100):
    print(i, x)

#while文
x = 1
while x < 1000:
    print(x, end='')
    x *= 2

#ネスト構造
for x in range(100):
    if x % 11 == 0:
        print(x, end='')

#break文
for x in range(10):
    if x == 5:
        break
    print(x, end='')