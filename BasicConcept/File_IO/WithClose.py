#with를 사용하면 close()안해도 autoclose가 된다. 
#close가 필요한 곳은 다 with를 쓰기

with open('서시1.txt', 'wt', encoding='UTF-8') as ptr :
    try :
        mystr = """
서시

죽는 날까지 하늘을 우러러
한점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.

오늘밤에도 별이 바람에 스치운다.
"""

        print(ptr.write(mystr), 'bytes saved')
    except :
        print('Exception 발생')

