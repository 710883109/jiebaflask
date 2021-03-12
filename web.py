# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template,request
import csv
import jieba
import json
from werkzeug.utils import secure_filename
from collections import OrderedDict
app = Flask(__name__)

@app.route("/")
def home():
    text=[]
#    with open('test.csv', encoding='utf-8') as csvfile:
# 讀取 CSV 檔案內容
#        rows = csv.reader(csvfile)
# 以迴圈輸出每一列
#        for row in rows:
#            print(row)
#            text.append(row[0])
#    print(text)
    return render_template('index.html',text=text)

@app.route("/textbox",methods=['POST'])
def llama():
    stringtext=request.values['text']
    #print(stringtext)
    seg_list = jieba.cut(stringtext, cut_all=True)
    print("seg_list",seg_list)
    autocut_list=[ stringtext[x:x+2] for x in range(len(stringtext)-1)] 
    print("autocut_list1",autocut_list)
    for i in range(len(stringtext)-2):
        autocut_list.append(stringtext[i:i+3])
    for i in range(len(stringtext)-3):
        autocut_list.append(stringtext[i:i+4])
    for i in range(len(stringtext)-4):
        autocut_list.append(stringtext[i:i+5])
    
    print("autocut_list",autocut_list)
    in_list=[]
    out_list=[]
    for item in seg_list:#模組切割的詞
        if len(item)>1:
            in_list.append(item)
    in_list=list(dict.fromkeys(in_list))
    print("in_list",in_list)

    for item in autocut_list:
        if item not in in_list:
            out_list.append(item)
    print("out_list1",out_list)
    out_list=list(OrderedDict.fromkeys(out_list))
    print("out_list",out_list)
    return render_template('sub1.html',text=in_list,t2=out_list,origin=stringtext)

@app.route("/upload",methods=['POST'])
def sheep():
    f = request.files['csvfile']
    fstring = f.read()
    #print(fstring)
    tmp=fstring.splitlines()
    #print(fstring.splitlines())
    
    text=[]
    for sentence in tmp:
        seg_list = jieba.cut(sentence, cut_all=True)
        text.append("/".join(seg_list))

    return render_template('index.html',text=text)
@app.route("/dua",methods=['POST'])
def goat():
    f = request.form.getlist('upload')
    print(f)
    out=json.dumps(f, ensure_ascii=False)
    return out 
app.run(host="0.0.0.0",port=7777,debug=True)
