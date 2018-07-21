import datetime
class inven:
	
	dateofpurchase= datetime.datetime.now()

	def __init__(self):
		items=['Soap','Chocolates','Cold-drinks','Fruits','Chips','Ice-cream']
		count=[50,20,30,25,20,20]
		price=[30,10,15,35,20,40]
		total=0
		print('Items in Inventory with price and availability:')
		for i in items:
			print ((i+1),' ',items[i],'-',count[i],' ',price[i],'Rupees')
		print('Enter the number of items you need:')
		for i in items:
			num[i]=int(input('Count of ',items[i],' you need'))
			rem[i]=count[i]-num[i]
		for i in items:
			cost[i]=num[i]*price[i]
			total+=cost[i]
		for i in items:
			count[i]=rem[i]
		print('final bill:')
		for i in items:
			print(i+1,items[i],' qty:',num[i],' ',price[i],' Rupees')
		print('Total: ',total)  

    
obj=inven()
obj.displ()
