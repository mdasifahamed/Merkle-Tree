nodes = [
    "A","B","C","D","E","F","G","H","I","J"
]

def pairnodes(arr):
    count = len(nodes)
    narr =[]
    pair=None
    while(len(nodes)>0):
        if(count%2!=0):
            pair = nodes[-1]+nodes[-1]
            del nodes[-1]
            count = count -1
        else:
            pair2 = nodes[0]+nodes[1]
            del nodes[0]
            del nodes[0]
            narr.append(pair2)
            pair2 = None 
    if(pair):
        narr.append(pair)
    return narr

print(pairnodes(nodes))


