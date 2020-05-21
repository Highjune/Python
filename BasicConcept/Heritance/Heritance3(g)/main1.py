from mammal import Mammal
from dog import Dog
from cat import Cat
from korean import Korean
from american import American

if __name__ == '__main__':
    mylist = [Dog('댕댕이'), Cat('새콤이'), Korean('한지민'), American('Michael')]
    #for mam in range(len(mylist)):
    #    mylist[mam].saySomething()
    for mam in mylist:
        mam.saySomething()