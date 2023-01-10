# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:44:54 2022

@author: Surface
"""
#13.1
import string
print(string.punctuation)

mystr="this is a banana."
mystr=mystr.replace("banana","orange")
print(mystr)
#replace方法的实现

mystr1="   this is a banana.    "
mystr1.strip()
print(mystr1.strip())
#strip方法的实现

mystr2="banana"
mystr2.translate("a")
print(mystr2)
#translate方法的实现

list2=[]#创建一个空列表
list1=["t","T","A","a","c"]#list1为一个假设的文件
for i  in list1:
    first=i.lower()
    list2.append(first)#取出list1每一个元素，转换为小写字母，然#后遍历添加到list2
print(list2)

#13.2

word_count={}
with open("C:\pg69642.txt",encoding="utf-8") as fin:
    for line in fin:
        line=line[:-1]#去除最后的换行符
        words=line.split()#空格进行分词，得到单词列表
        for word in words:
            if word not in word_count:
                word_count[word]=0#没出现过的单词，其value初始化为0，随后加一
            word_count[word]+=1
print(word_count)#打印每个单词出现的次数

#计算单词总数
import re
with open("C:\pg69642.txt",encoding="utf-8") as fin:
     content=fin.read()
words1=re.split((r"[\s.()-?]+"),content)
print(len(words1))




#13.3
import re#引入正则表达式模块
with open("C:\pg69642.txt",encoding="utf-8") as fin:
     content=fin.read()

#print(re.split((r"[\s.()-?]+"),content))
words=re.split((r"[\s.()-?]+"),content)
print(len(words))#计算单词数量
#import pandas as pd
#print(pd.Series(words).vaule_counts()[:20])
#print(words)
import pandas as pd
print(pd.Series(words).value_counts()[:20])#打印出现频率前20的单词

    