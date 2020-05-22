import sys
import printmenu
import create
import output
import filesave 
import load
import search
import delete
import update

def main():
    try:
        mylist = load.load_customer()
    except Exception as ex: 
        print(ex.args[0])
    else :
        pass
        #print('데이터 파일이 잘 loading 됐습니다.')
        
    while True :
        menu = printmenu.print_menu()
        if menu == 1 :
            mycustomer = create.create_customer()
            mylist.append(mycustomer)
            
        elif menu == 2 : 
            output.show_customer(mylist)
            
        elif menu == 3 :
            mycustomer = search.search_customer(mylist)
            if mycustomer == None : print('찾지 못했습니다.')
            else  : delete.delete_customer(mylist, mycustomer)
            
        elif menu == 4 : 
            mycustomer = search.search_customer(mylist)
            if mycustomer == None : print('찾지 못했습니다.')
            else  :print(mycustomer)
            
        elif menu == 5 : 
            mycustomer = search.search_customer(mylist)
            if mycustomer == None : print('찾지 못했습니다.')
            else  : update.update_customer(mycustomer)
        elif menu == 6 : 
            filesave.save_csv(mylist)
            
        elif menu == 9 :
            print('Program is Over...')
            filesave.save_customer(mylist)
            sys.exit(0)


if __name__ == '__main__':
    main()