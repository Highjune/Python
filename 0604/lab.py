import qrcode

url = 'https://www.naver.com'

img = qrcode.make(url)
print(img)
img.show()