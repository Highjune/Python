import xml.etree.ElementTree as ET

xml_ = ET.parse('../books.xml') #file에서 memory로 loading
# print(type(xml_)) #ElementTree 
root = xml_.getroot() #Element - 우리가 핸들링 하는 것
# print(type(root))
# print(root.tag)

# books = root.getchildren() #쓰지 않기로 권장. 'this method will be deleted in future versions

books = list(root)
# for book in books:
#     print(book.tag, book.key(), book.items()) #Element Name

#값이 바뀔 수 있으면 childelement
#값이 바뀌지 않으면 attribute

# print(books[0].items())

for book in books:
    print(book.tag, '-->', book.attrib) 