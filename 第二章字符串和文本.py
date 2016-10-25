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
    ###match
import re
text1="10/19/2016"
text2="Oct 19 ,2016"
print(re.match(r'\d+/\d+/\d+',text1))#<_sre.SRE_Match object; span=(0, 10), match='10/19/2016'>
print(re.match(r'\d+/\d+/\d+',text2))#None
#########想要将一种模式匹配多次，则可以先用compile定义匹配模式
modle=re.compile(r'\d+/\d+/\d+')
print(modle.match(text1))#<_sre.SRE_Match object; span=(0, 10), match='10/19/2016'>
print(modle.match(text2))#None
#########match 总是从左到右从头开始匹配，如果向对全局进行匹配，则可以用findall,返回的时匹配成功的序列
text="Today is 10/19/2016,pycon starts 11/11/2016"
print(modle.findall(text))#['10/19/2016', '11/11/2016']
#########通过捕获组可以简化匹配之后数据的处理
modle=re.compile(r'(\d+)/(\d+)/(\d+)')
result=modle.match(text1)
print(result.group(0))#10/19/2016
print(result.group(1))#10
print(result.group(2))#19
print(result.group(3))#2016
result=modle.findall(text)
print(result)#[('10', '19', '2016'), ('11', '11', '2016')]通过分组使得捕获之后数据呈现成了元组所组成的序列，便于之后的数据处理
for mon,day,year in result:
    print("{0}-{1}-{2}".format(mon,day,year))
                            ########10-19-2016
                            #########11-11-2016
########如果想用迭代的方式找到匹配项并返回元组序列，则可以使用finditer
for result in modle.finditer(text):##迭代器最好和for一起使用
    print(result.groups())#('10', '19', '2016')  ('11', '11', '2016')

#2.5查找和替换文本
#######re.sub
import re
text="25/10/2016,11/11/2016"
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\2-\1',text))###2016-10-25,2016-11-11    sub实际上是先把datepat的模式应用于text进行匹配，匹配的结果传入r'\3-\2-\1'这个表达式
########更高级的用法时直接把r'\3-\2-\1'替换成回掉函数
#
from calendar import  month_abbr  ####month_abbr 接受月份的int值作为输入参数，输出英文简写，如输入3 输出Mar
def change_date(m):
    man_name=month_abbr[int(m.group(2))]
    #print(m.group(2))
    return '{0} {1} {0} {2}'.format(m.group(1),man_name,m.group(3))
print(datepat.sub(change_date,text))###25 Oct 25 2016,11 Nov 11 2016