# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:41:49 2022

@author: Surface
"""
#13.4
import re#引入正则表达式模块
with open("C:\words.txt",encoding="utf-8") as fin:
    content=fin.read()
words=re.split((r"[\s.()-?/]+"),content)
words=set(words)


with open("C:\pg69642.txt",encoding="utf-8") as fin:
    content=fin.read()
words1=re.split((r"[\s.()-?]+"),content)
words1=set(words1)

words2=words-words1
print(words2)












































