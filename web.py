from flask import Flask
from flask import render_template,request
import csv
import jieba
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/")
def home():
    text=[]
    with open('test.csv', encoding='utf-8') as csvfile:
# 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
# 以迴圈輸出每一列
        for row in rows:
            print(row)
            text.append(row[0])
    print(text)
    return render_template('index.html',text=text)

@app.route("/textbox",methods=['POST'])
def llama():
    stringtext=request.values['text']
    seg_list = jieba.cut(stringtext, cut_all=True)
    return render_template('index.html',text=seg_list)

@app.route("/upload",methods=['POST'])
def sheep():
    f = request.files['csvfile']
    fstring = f.read()
    print(fstring)
    print(fstring.splitlines())
    #text=[]
    '''
    #filename = secure_filename(file.filename)
    #file.save('./', filename)
    with open('filename', encoding='utf-8') as csvfile:
# 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
# 以迴圈輸出每一列
        for row in rows:
            print(row)
            text.append(row[0])
    print(text)
    seg_list = jieba.cut(text[0], cut_all=True)
    '''
    seg_list = jieba.cut(fstring, cut_all=True)
    return render_template('index.html',text=seg_list)
app.run(host="0.0.0.0",port=7777,debug=True)