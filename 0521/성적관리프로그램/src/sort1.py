#sort1.py : Selection Sorting

def selectionSort(mylist):
    for i in range(len(mylist) - 1):
        for j in range(i + 1, len(mylist)):
            if mylist[i].total > mylist[j].total : 
                mylist[j].ranking += 1
            elif mylist[i].total < mylist[j].total : 
                mylist[i].ranking += 1
