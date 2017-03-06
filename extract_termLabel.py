#-*-coding:utf-8-*-#
from xml.dom.minidom import parse
import xml.dom.minidom
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

term_label_out=open('term_label','wb')
# translated=open('result.txt','r')
# trans=translated.readlines()
#使用minidom解析打开xml文档
DOMTree=xml.dom.minidom.parse("stTranslationRecords-1.xml")
Root=DOMTree.documentElement
if Root.hasAttribute("xmlns:stkosbase"):
    print "root element:%s"%Root.hasAttribute("xmlns:stkosbase")
#集合中获取所有的Record
RecordInfor=Root.getElementsByTagName("stkosbase:StTranslationRecord")
count=0
for record in RecordInfor:
    Term=record.getElementsByTagName("stkosbase:termLabel")[0]
    T=Term.childNodes[0].data
    T=''.join(re.findall('[a-zA-Z0-9()\-ΣΔαβγδμГПⅡⅥⅢⅤVVIⅣ（）.+,, ]+',T))
    term_label_out.write(T+"\n")
    count+=1
    print "processing the ",count, "record"
term_label_out.close()
