#delete.py
def delete_customer(mylist, mycustomer):
    for idx, n in enumerate(mylist):
        if n.name == mycustomer.name : 
            del mylist[idx]
            print('삭제 성공')
            break