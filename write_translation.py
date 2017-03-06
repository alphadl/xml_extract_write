#-*-coding:utf-8-*-#

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse,Element
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xml_doc=parse('stTranslationRecords-1.xml')

read_translation=open('result.txt','r')
result=read_translation.readlines()
print len(result)

root=xml_doc.getroot()
index=0
# for child in root[0]:
#     print child.tag,"###",child.attrib,"###",child.text
for trans in root.iter('{http://www.nstl.gov.cn/stkos/stkosbase/1.0}translationText'):
    print trans.tag
    trans.text=str(result[index]).replace(' ', '')
    print trans.text
    print "正在写入第",index+1,"条数据"
    index+=1
print "写入完成",index,"条记录"
xml_doc.write('translated.xml',encoding='utf8',method='xml')
# node=xml_doc.find('./stkosbase:translationText')

# print type(node),len(node)