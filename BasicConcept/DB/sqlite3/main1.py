import xml.etree.ElementTree as ET

# xml_ = ET.parse("books.xml")
# root = xml_.getroot()

#위와 같다.(단지 밑은 처음부터 element로 뽑은 것임)
# root = ET.Element(file = 'books.xml')


xml_ = ET.parse("books.xml")
root = xml_.getroot()
books = root.findall("book")
for book in books:
    print(book.find('author').text, book.find('title').text, book.find('price').text)