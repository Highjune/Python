from telephone import Telephone as tel

jimin = Telephone('한지민 25 010-2345-4562')
june = Telephone('허강준 35 010-2325-4517')
hee= Telephone('한지희 45 010-2315-4564')
mylist = [jimin, june, hee]

for n in range(len(mylist)):
    print(mylist[n])
