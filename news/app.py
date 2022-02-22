# -*- codeing = utf-8 -*-
# @Time : 2022/2/16 11:40
# @Author : xiaoHei
# @File : app.py.py
# @Software : PyCharm

from flask import Flask,render_template
import os,json

app = Flask(__name__)

rootdir = 'E:\\workspace\\shiyanlou_zxwz\\files'
@app.route('/')
def index():
    #显示文章名称的列表
    # 也就是 /home/shiyanlou/files/ 目录下所有 json 文件中的 `title` 信息列表
    list = os.listdir(rootdir)  # 列出文件夹下所有的目
    title_list=[]
    for i in list:
        path = os.path.join(rootdir, i)
        if os.path.isfile(path):
            with open(path,'r',encoding='utf-8') as fp:
                content = json.load(fp)
                title_list.append(content['title'])
    return render_template('index.html', title=title_list)


@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面
    lujing = rootdir.join(filename)
    print(lujing)
    with open(rootdir+'\\'+filename+'.json','r',encoding='utf-8') as fp:
        content = json.load(fp)
    return render_template('file.html',content=content)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run('127.0.0.1','8080',1)