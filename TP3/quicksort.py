
def compare(a,b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def partition(pivot, list, comp=compare):
    if list == []:
        return ([],[])
    else:
        list1, list2 = partition(pivot,list[1:],comp=comp)
        cmp=comp(list[0], pivot)
        if cmp < 1:
            return ([list[0]] + list1 , list2)
        else:
            return (list1 , [list[0]] + list2)

def quicksort(list, comp=compare):
    n = len(list)
    if n <= 1:
        return list.copy()
    else:
        list1, list2 = partition(list[0], list[1:], comp=comp)
        list1s = quicksort(list1, comp=comp)
        list2s = quicksort(list2, comp=comp)
    return list1s + [list[0]] + list2s    

list=[5,8,2,1,3,9,8,7,3,5,0]
print(quicksort(list, compare))    