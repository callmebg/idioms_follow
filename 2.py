# -*- coding:utf-8 -*-
import csv
headers = ["成语","长度","拼音","成语解释","出自","去调拼音","首字拼音","末字拼音"]
data = []
data_sum = 30957
mydata = []

now_sum = 0 	#已经处理的成语数
every = []

def init():
	with open('cyyy.csv',mode = 'r',encoding = 'utf-8')as f:
		global data
		data = csv.DictReader(f)
		#print(type(data))
		i = 0
		for aline in data:
			temp = {'编号': i}	#每个成语的唯一编号
			i += 1
			j = 0
			for elem in aline.values():
				temp[headers[j]] = elem
				j += 1
			mydata.append(temp)
	print(len(mydata))	
	for i in range(data_sum):
		mydata[i]['深度'] = -1
		mydata[i]['上一个'] = 0
		ok = True
		for j in range(data_sum):
			if i != j:
				if mydata[i]['末字拼音'] == mydata[j]['首字拼音']:
					ok =False
					break
		if ok:
			global now_sum
			now_sum += 1
			mydata[i]['深度'] = 0
			print(mydata[i]['成语'] + " " + mydata[i]['末字拼音'])
	every.append(now_sum)
	bfs(1)
	for i in every:
		print(i)
	for i in range(data_sum):
		t = []
		t.append(mydata[i]['编号'])
		t.append(mydata[i]['成语'])
		t.append(mydata[i]['长度']) 
		t.append(mydata[i]['拼音'])
		t.append(mydata[i]['成语解释'])
		t.append(mydata[i]['出自']) 
		t.append(mydata[i]['去调拼音'])
		t.append(mydata[i]['首字拼音'])
		t.append(mydata[i]['末字拼音'])
		t.append(mydata[i]['深度'])
		t.append(mydata[i]['上一个'])

		with open('cyyyy.csv',mode = 'a',newline = '',encoding = 'utf-8')as f:
			f_csv = csv.writer(f)
			f_csv.writerow(t)

def bfs(deep):
	global now_sum
	last = now_sum
	if now_sum >= data_sum:
		return
	else:
		for i in range(data_sum):
			if now_sum >= data_sum:
				break
			if mydata[i]["深度"] == -1:
				for j in range(data_sum):
					if mydata[j]["深度"] == deep - 1:
						if mydata[i]['末字拼音'] == mydata[j]['首字拼音']:
							now_sum += 1
							mydata[i]["深度"] = deep
							mydata[i]['上一个'] = j
							break
		every.append(now_sum - last)
		bfs(deep + 1)

def menu():
	print("按1进入成语解释")
	print("按2进入成语接龙(快速接到末尾)")
	print("按其他键退出程序")
	return int(input())

def explain():
	print("输入一个成语")
	find_str = str(input()).encode('utf-8')
	for i in mydata:
		if i["成语"].encode('utf-8') == find_str:
			#print("okk")
			for j in range(5):
				print(headers[j]+": "+i[headers[j]])
			return
	print("并没有找到该成语\n")

def idioms_follow():
	pass
if __name__ == "__main__":
	init()
	while(True):
		choice = menu()
		if choice == 1:
			explain()
		elif choice == 2:
			idioms_follow()
		else:
			break
	input("按任意键结束")
	input("按任意键结束")
	input("按任意键结束")