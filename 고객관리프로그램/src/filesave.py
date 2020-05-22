#filesave.py
import pickle
import csv

def save_customer(mylist):
    with open('customers.data', 'wb') as ptr:
        try:
            pickle.dump(mylist, ptr)
        except Exception as e: 
            print('Exception 발생  = ', e.args[0])
        else : 
            print('Save Successfully')
    
def save_csv(mylist):
    try:
        backup_file = input('Backup할 파일 이름 : ')
        ptr = open(backup_file, 'wt', newline='', encoding = 'utf-8')
        mywriter = csv.writer(ptr, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for customer in mylist:
            mywriter.writerow(customer.getInfo())
    except :
        print('CSV File Save Exception')
    else :
        print(backup_file, '에 잘 저장됐습니다.')
    finally : 
        ptr.close()