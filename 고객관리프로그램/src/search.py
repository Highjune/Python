def search_customer(mylist):
    username = input("찾으시는 고객의 이름 : ")
    result = None
    for idx, mycustomer in enumerate(mylist):
        if mycustomer.name == username :
            result = mylist[idx]
            break
            
    if idx < len(mylist) : return result
    else : return None