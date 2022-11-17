class Item:
    def __init__(self,value,weight):
        self.weight=weight
        self.value=value

def fraKnapsack(arr,W):
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
    finalValue=0.0
    count=0.0
    list=[]
    list1=[]
    
    for item in arr:
        if item.weight<=W:
            W -= item.weight
            finalValue += item.value
            count=1.0
            list.append(count)
            list1.append(finalValue)
        else:
            count =W/item.weight
            list.append(count)
            finalValue += (W*item.value/item.weight)
            list1.append(W*item.value/item.weight)
            break
    return finalValue,list,list1

arr=[Item(60,10),Item(100,20),Item(120,30)]
W=50
finalValue,list,list1=fraKnapsack(arr,W)
print(finalValue)
print(list)
print(list1)