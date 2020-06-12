def part(pivot,list):
    items_greater = []
    items_lower = [] 
    i = 0
    while i < len(list):
        if list[i] > pivot:
            items_greater.append(list[i])
        else:
            items_lower.append(list[i])
        i += 1
    return items_lower + [pivot] + items_greater        

def qs(list):
    length = len(list)
    if length <= 1:
        return list
    else: 
        pivot = list.pop()    

    items_greater= [] 
    items_lower= []
    i = 0
    while i < len(list):
        if list[i] > pivot:
           items_greater.append(list[i])
        else:
           items_lower.append(list[i])
        i = i + 1
    
    return qs(items_lower) + [pivot] + qs(items_greater)   

list=[5,8,2,1,3,9,8,7,3,5,0]
print(part(4,list))