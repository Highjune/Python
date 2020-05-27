import xml.etree.ElementTree as ET
from idlelib.iomenu import encoding

xml_ = """
<books>
    <book id = '2020-01'>
        <author>한지민</author>
        <title>Beginning Python</title>
        <price>25000</price>
    </books>

    <book id = '2020-02'>
        <author>허강준</author>
        <title>JAVA</title>
        <price>35000</price>
    </books>
</books>
"""

# ET.dump(xml_) #메모리상에서 저장하면 dump. 파일로 내보내려면 write

#파일을 메모리에 로딩할 떄 parse, getroot

#xml을 변환할 때때 
elem_ = ET.fromstring(xml_)  #1. 문자열->element
tree = ET.ElementTree(elem_) #2. element->elementTree  이 2가지를 다 해야지 xml로 만들 수 있다.
tree.write("mybooks.xml", encoding = 'utf-8')


