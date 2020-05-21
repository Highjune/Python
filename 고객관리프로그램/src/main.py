import sys
import printmenu
import create
import output
import filesave
def main():
    mylist = []
    while True :
        menu = printmenu.print_menu()
        if menu == 1 :
            mycustomer = create.create_customer()
            mylist.append(mycustomer)
            
        elif menu == 2 : 
            output.show_customer(mylist)
            
        elif menu == 3 :
            pass
        elif menu == 4 : 
            pass
        elif menu == 5 : 
            filesave.save_customer(mylist)
        elif menu == 9 :
            print('Program is Over...')
            sys.exit(0)


if __name__ == '__main__':
    main()