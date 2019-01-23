
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [] # 你可以用 products.append([name, price])
	p.append(name)#取代以下四行 把小清單裝進大清單
	p.append(price)
	products.append(p)
print(products)#
products[0][0]#將大清單的第一個數字取出再取出小清單的第一個數字
print(products[0][1])
