#2.1针对任意多的分隔符拆分字符串
import re
line="axascd,cdscsv  asfcdsvcf,xascdvf;cdsvfd,sfvdv     acdvf"
lines=re.split(r'[,;\s]\s*',line)
print(lines)#['axascd', 'cdscsv', 'asfcdsvcf', 'xascdvf', 'cdsvfd', 'sfvdv', 'acdvf']
      ####需要注意的是使用了捕获组的话，分隔符也会存在于结果中
lines=re.split(r'(,|;|\s)\s*',line)
print(lines)#['axascd', ',', 'cdscsv', ' ', 'asfcdsvcf', ',', 'xascdvf', ';', 'cdsvfd', ',', 'sfvdv', ' ', 'acdvf']
#2.2在字符串的开头或结尾处做文本匹配
import os
filenames=os.listdir(".")
print(filenames)
print([name for name in filenames if name.endswith(('.c','.h','.py'))])
print(any(name.endswith('.py') for name in filenames))#any(iterable)   如果iterable的任何元素不为0、''、False,all(iterable)返回True。如果iterable为空，返回False
#可以理解any为并集，而all为交集，any当所有元素中都为0、''、False时才为false，而all则只要是其中一个元素为0、''、False则为false

#2.3利用shell通配符做字符串匹配
        #fnmatch根据所在底层操作系统来决定是否关注大小写
        #fnmatchcase严格区分大小写，无论底层是什么操作系统
from fnmatch import fnmatch,fnmatchcase
print("fnmatch result is {0}".format(fnmatch("helloworld.c","*.C")))#fnmatch result is True
print("fnmatchcase result is {0}".format(fnmatchcase("helloworld.c","*.C")))#fnmatchcase result is False
#####需要注意的是fnmatch更多的是用于提供一种简单的机制在处理数据时允许使用通配符来匹配，而若是应用中想匹配文件名则应该考虑glob


#2.4文本模式的匹配和查找

