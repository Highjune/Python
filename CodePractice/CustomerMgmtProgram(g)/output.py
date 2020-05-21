#output.py

def show_customer(mylist):
    print('-' * 40)
    print('고 객 정 보 리 스 트')
    print('-' * 40)
    print('GRADE NAME PHONE EMAIL AGE ETC')
    print('-' * 40)
    for customer in mylist:
        print(customer)