# -*- coding:utf8 -*-
import csv
headers = ["编号","成语","长度","拼音","成语解释","出自","去调拼音","首字拼音","末字拼音","深度","下一个"]
data_sum = 30957
mydata = []

def init():
    global mydata
    with open('cyyyy.csv',mode = 'r',encoding = 'utf-8')as f:
        data = csv.DictReader(f)
        for aline in data:
            temp = {}
            for i in range(11):
                temp[headers[i]] = aline[headers[i]]
            mydata.append(temp)

def menu():
    print("1、成语解释")
    print("2、成语接龙(快速接到末尾)")
    print("3、查询以某个拼音开头的成语")
    print("4、查询以某个拼音结尾的成语")
    print("5、关于")
    print("按其他键退出程序")
    return int(input())

def explain():
    print("输入一个成语")
    find_str = str(input()).encode('utf-8')
    for i in mydata:
        if i["成语"].encode('utf-8') == find_str:
            for j in range(7):
                print(headers[j]+": "+i[headers[j]])
            return
    print("并没有找到该词\n")

def idioms_follow():
    print("输入一个成语")
    find_str = str(input()).encode('utf-8')
    code = -1
    for i in range(data_sum):
    	if mydata[i]["成语"].encode('utf-8') == find_str:
            code = i
    if code == -1:
        print("并没有找到该词\n")
    else:
        while True:
            print(mydata[code]["成语"],end = '》》')
            if int(mydata[code]["深度"]) == 0:
                break
            else:
                code = int(mydata[code]["下一个"])
        print("结束")

def find_head():
    print("输入开头音节")
    find_str = str(input())
    sum = 0
    ans = []
    for i in range(data_sum):
        if mydata[i]["首字拼音"] == find_str:
            sum += 1
            ans.append(i)
    if sum == 0:
        print("并没有找到该音节开头的成语\n")
    else:
        print("以该音节开头的成语一共有 " + str(sum) + " 个")
        for i in ans:
            print(mydata[i]["成语"])

def find_tail():
    print("输入结尾音节")
    find_str = str(input())
    sum = 0
    ans = []
    for i in range(data_sum):
        if mydata[i]["末字拼音"] == find_str:
            sum += 1
            ans.append(i)
    if sum == 0:
        print("并没有找到该音节结尾的成语\n")
    else:
        print("以该音节结尾的成语一共有 " + str(sum) + " 个")
        for i in ans:
            print(mydata[i]["成语"])

def about():
    print("关于：")
    print("1.该软件不定时更新的地址在：")
    print("2.该软件词库一共30957个词，可在cyyyy.csv自行修改")
    print("3.b站视频地址：")
    print("4.csdn博客地址：")
if __name__ == "__main__":
    init()
    while(True):
        choice = menu()
        if choice == 1:
            explain()
        elif choice == 2:
            idioms_follow()
        elif choice == 3:
            find_head()
        elif choice == 4:
            find_tail()
        elif choice == 5:
            about()
        else:
            break