#filesave.py
def save_customer(mylist):
    path = input('저장할 파일 이름 : ')
    with open(path, 'at', encoding = 'utf-8') as ptr:
        try:
            for customer in mylist:
                ptr.writelines(str(customer))
                ptr.writelines('\n')
        except Exception as e: 
            print('Exception 발생  = ', e.args[0])
        else : 
            print('Text 파일이 잘 저장되었습니다. 파일이름 : ', path)
    