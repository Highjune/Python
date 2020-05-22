from os.path import exists
import pickle

def load_customer():
    mylist = []
    try:
        if exists('customers.data') :  #파일이 있다면
            with open('customers.data', 'rb') as ptr:
                mylist = pickle.load(ptr)
        else : 
            raise FileNotFoundError("첫 사용자이지요?")
    except Exception as ex:
        print('Exception 발생 : ', ex.args[0])
    return mylist