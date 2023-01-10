# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:16:34 2023

@author: Surface
"""
#13.6
import re
with open("C:\pg69642.txt",encoding="utf-8") as fin:
    content=fin.read()

#print(re.split((r"[\s.()-?]+"),content))
words=re.split((r"[\s.()-?/]+"),content)
words1={"a","the","and","of","to","in","was","that","her","as","he","his","had","with","it",
        "on","for","not","she"}
#找了上个作业同样的模板，只不过这次的word1为一个集合

words=set(words)
#把words列表转换为一个集合
words2=words-words1
#使用集合里面的差集计算，直接相减
print(words)
#打印差集的值



    



