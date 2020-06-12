# from ap2_decorators import trace
# from ap2_decorators import count

# @trace
# def split(list):
#     n = len(list)
#     if n == 0:
#         return ([],[])
#     elif n == 1:
#         return ([list[0]], [])
#     else:
#         list1, list2 = split(list[2:])
#         return ([list[0]]+list1,[list[1]]+list2)

# print(split([4,9,6,8,7,5,2,3,4,8,0]))
def compare(a,b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def merge(list1, list2, comp=compare):
    if list1 == []:
        return list2.copy()
    elif list2 == []:
        return list1.copy()
    else:
        cmp = comp(list1[0],list2[0])
        if cmp <= 0:
            return [list1[0]] + merge(list1[1:], list2, comp=comp)
        else:
            return [list2[0]] + merge(list1, list2[1:], comp=comp)   
        
def mergesort(list):
     if(len(list) <= 1):
         return list
     mid = int(len(list)/2) 
     left = mergesort(list[:mid])  
     right = mergesort(list[mid:])
     return merge(left,right,comp=compare) 

print(mergesort([4,9,6,8,7,5,2,3,4,8,0]))
