#-*- coding:utf8 -*-
import csv
import json
import random
from flask import Flask,render_template,request

headers = ["编号","成语","长度","拼音","成语解释","出自","去调拼音","首字拼音","末字拼音","深度","下一个"]
data_sum = 30957    #默认值
mydata = []
#head = '<head> <meta charset="utf-8" /> </head>'

def init():
    global mydata, data_sum
    with open('cyyyy.csv',mode = 'r',encoding = 'utf-8')as f:
        data = csv.DictReader(f)
        for aline in data:
            temp = {}
            for i in range(11):
                temp[headers[i]] = aline[headers[i]]
            mydata.append(temp)
        data_sum = len(mydata)

def explain(word):
    find_str = str(word).encode('utf-8')
    ans = {'status':0, 'msg' : 'Not found in my database.', 'data' : {'num' : 7}}
    for i in mydata:
        if i["成语"].encode('utf-8') == find_str:
            ans['status'] = 1
            ans['msg'] = 'succes'
            for j in range(7):
                #print(headers[j]+": "+i[headers[j]])
                ans['data'] [headers[j]] = i[headers[j]]
            #print("")
    #print("并没有找到该词\n")
    return json.dumps(ans)

def idioms_follow(word):
    find_str = str(word).encode('utf-8')
    code = -1
    ans = {'status':0, 'msg' : 'Not found in my database.', 'data' : {'num' : 0}}
    for i in range(data_sum):
    	if mydata[i]["成语"].encode('utf-8') == find_str:
            code = i
    if code == -1:
        #print("并没有找到该词\n")
        pass
    else:
        ans['status'] = 1
        ans['msg'] = 'succes'
        t = 0
        while True:
            #print(mydata[code]["成语"],end = '》》')
            ans['data'][t] = mydata[code]["成语"]
            t = t + 1
            if int(mydata[code]["深度"]) == 0:
                break
            else:
                code = int(mydata[code]["下一个"])
        #print("结束\n")
        ans['data']['num'] = t
    return json.dumps(ans)
    

def rand():
    json.dumps(mydata[random.randint(0,data_sum)]["成语"])

def about():
    print("关于：")
    print("1.该软件不定时更新的地址在：https://github.com/callmebg/idioms_follow")
    print("2.该软件词库一共" + str(data_sum) + "个词，可在cyyyy.csv自行修改")
    print("3.b站视频地址：https://www.bilibili.com/video/av63639474/")
    print("4.csdn博客地址：https://blog.csdn.net/qq_34438779/article/details/99469079")
    print("")


app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return 'hello world!'

@app.route('/admin')
def admin():
    return '我还没开始写呢。。。'

@app.route('/api_IF/',methods=['GET','POST'])
def api_IF():
    if request.method == 'GET':
        return '''本API为成语接龙API，可以把一个成语迅速接到不能接为止<br>
        您可以通过POST的方式传递名为word的变量成语来获取json格式结果<br>
        例如传入“笔走龙蛇”，将返回<br>
        {<br>
            status: 1,<br>
            msg: "succes",<br>
            data:{<br>
                num: 2,<br>
                0: 舍己救人,<br>
                1: 人涉卬否<br>
            }<br>
        }<br>
        status：1:正常返回结果，0则为异常
        msg：当前请求返回状态说明，如"ok" "Not found in my database"
        data: {
            num：成语后接龙的数目
            0：第一个成语
            1：第二个成语
            ...
            n-1:最后一个成语
        }
        '''

    else:
        word = request.form.get('word')
        ans = idioms_follow(word)
        return ans
@app.route('/api_explain',methods=['GET','POST'])
@app.route('/api_explain/',methods=['GET','POST'])
def api_explain():
    if request.method == 'GET':
        return '''本API为成语解释API，可以把一个成语迅速接到不能接为止<br>
        您可以通过POST的方式传递名为word的变量成语来获取json格式结果<br>
        例如传入“笔走龙蛇”，将返回<br>
        {<br>
            status: 1,<br>
            msg: "succes",<br>
            data:{<br>
                编号: 1865,<br>
                成语: "笔走龙蛇",<br>
                长度: 4,<br>
                拼音："bǐ zǒu lóng shé",<br>
                成语解释："形容书法生动而有气势。",<br>
                出自："唐·李白《草书歌行》：“时时只见龙蛇走，左盘右蹙旭惊电。”",<br>
                去调拼音："bi zou long she"<br>
            }<br>
        }<br>
        status：1:正常返回结果，0则为异常
        msg：当前请求返回状态说明，如"succes" "Not found in my database"
        编号为我数据库内成语的编号
        '''
    else:
        word = request.form.get('word')
        ans = explain(word)
        return ans

if __name__ == "__main__":
    init()
    app.run(host='0.0.0.0',port=80)
    #app.run(debug=True)
