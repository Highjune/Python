from telephone import Telephone

jimin = Telephone('한지민,25,010-2345-6789')
chulsu = Telephone('김철수,35,010-2345-1111')
younghee = Telephone('이영희,45,010-5555-6789')
mylist = [jimin, chulsu, younghee]

for n in range(len(mylist)):
    print(mylist[n])