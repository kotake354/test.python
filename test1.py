#pythonの文法～データー構造
#文字列長さ
f = ("いろはにほへと")
print(len(f))

#文字列と演算
s = ('long'*2+'ago')
print(s)

#演算
b = (100+200)
print(b)

#インデックスとスライス
x = ("abcde")
print(x[0])
food = ("applepie")
print(food[:5])

#リスト
menu = ["cherry", "pasta", "steak"]
print(menu)

#リストの連結
a = ['beef', 'pork']
print(a[0])
b = ['chicken', 'vegetable']
c = a+b
print(c)

#リスト　要素追加、
menu.append("parfait")
print(menu)
#挿入
menu.remove("pasta")
print(menu)
#削除
menu.insert(2, "salad")
print(menu)
#ポップを使って削除
print(menu.pop(1))
#要素数の取得
print(len(menu))

#タプル
u = ("curry" , 860 , 847.4)
print(u)
#インデックス
print(u[1])
#スライス
print(u[0:1])
print(u[1:2])
print(u[0:-1])

#パック
m = "doria", 1190
print(m)
#アンパック
name, price = m
print(name)
print(price)

#リストとタプル
menu1 = [('curry', 860) , ('doria' , 1190) , ('stek' , 1460)]
print(menu1)
print(menu1[1])
print(price)
print(name)

#集合の初期化
color = {'red' , 'green' , 'blue'}
print(color)

#in演算子とnon in演算子
print('green' in color)
print('black' in color)

color1 = {'yellow' , 'pink' , 'black'}
print(color1)

print('red' not in color)
print('black' not in color)

#要素の追加と削除（ミュータブルなので要素の追加と削除可能）
color |= {'black' , 'white'}
print(color)
#addメゾットを使って前述の変巣に（集合.add(値)）でも追加可能
color.add('pink')
print(color)
#削除
color -= {'green'}
print(color)
#removeメゾットを使って前述の変巣に（集合.remove(値)）でも追加可能
color.remove('red')
print(color)

#集合に対する色々な演算

w = {'red' , 'green' , 'blue'}
q = {'green' , 'black' , 'white'}
#集合w&集合q　積集合（集合wと集合qに共通する要素を持つ集合）
print(w&q)
#集合w|集合q　和集合（集合wと集合qの全ての要素を持つ集合）
print(w|q)
#集合w-集合q　差集合（集合wから集合qの要素を削除した集合）wから、qと同じものを引き算してwの残った値が出る
print(w-q)
#集合A^集合B　対象差（集合Aまたは集合Bの一方だけが含む要素の集合）
print(w^q)

#辞書の初期化
prefix = {'kiro' : 1000, 'mega' : 1000000}
print(prefix)

#辞書に要素の追加
prefix['giga'] = 1000000000
print(prefix)

#辞書内の要素の削除
del prefix['kiro']
print(prefix)

#辞書内の要素の有無
print('kiro' in prefix)
print('kiro' not in prefix)
print('mega' in prefix)
print('mega' not in prefix)