try :
    ptr = open('서시.txt', 'wt', encoding='utf-8' ) #writetext
except Exception as e: 
    print("Exception 발생했음.", e.args[0])
else :
    str = """
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

    print(ptr.write(str))  #write는 사이즈를 알려준다.
    print('Save Successfully')
finally :
    ptr.close()
#실행 후 refresh하면 '서시.txt' 생성




