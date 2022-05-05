from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

#itemsets=["134","235","1235","25"]
itemsets=["1234","12345","234","235","124","134","2345","1345","345","1235"]
c1={} # Empty dictionary created for c1
l1={} # Empty dictionary created for l1
a=set()
frequent=[]
for w in itemsets: #pick each item from itemset
    for i in range(len(w)): # for length of each item in itemset iterate the loop
        if w[i] in c1:  #check if each index of item picked from itemset exist in dictionary
            c1[w[i]]=c1[w[i]]+1 #if yes then increment the value by 1 
        else:
            c1[w[i]]=1 #if not exist then add a new entry

support=30 #consider support is 30
support=support/100 *len(itemsets)


for w in c1: # those with support greater than given will be added to l1
    if c1[w] >= support:
        l1[w]=c1[w]

for s in range(4):
    frequent.append(l1) #add every time l1 to frequent list
        
    count=1
    key=list(l1.keys()) # make list of all keys in l1
    
    del c1 # delete the existing candidate set to populate it with new values from l1
    c1={} # create empty c1
    
    for w in l1: # making pairs
        if len(w)%2==0:   
            a=set(w) # only we can make pairs if the items have specified values in common  
            for i in range(len(l1)-count):  # we will move forwad till end from point where we are in the loop of l1
                b=set(key[i+count]) # pick next item relative to current item and convert it to set also 
                if len(a & b)==len(w)-1: # now check if intersection of these consecutive items is equal to one less than length of w
                    #now we have to check that all subsets of pair should be present in l1 to add it to candidate set 
                    pair=str(w+""+''.join(str(s) for s in (b-a)))
                    powersets=list(powerset(tuple(pair))) #power sets generated, because all subset of frequent item sets should be frequent
                    for k in range(len(powersets)): #Start traversing list of all power sets 
                        tupletostring=''.join(powersets[k]) # pick kth item from powerset and convert this tuple to string
                        if len(tupletostring)==len(w): # now if length of this subset is equal to length of w
                            print("tupletostring : ",tupletostring)
                            aa=set(tupletostring)
                            if tupletostring not in l1: # then check 
                                break
                        if k+1==len(powersets):
                             c1[pair]=0 
                    print("powersets",powersets)
        else:    
            for i in range(len(l1)-count):  
                c1[w+""+key[i+count]]=0
            count=count+1   
        
    del l1 # now we have pairs present in c1 , delete l1 to populate it with frquent pairs
    l1={}
    #now create l1 from c1
    for w in c1: # find support of each item in c1 by matching it with itemsets
        for i in itemsets:
            for j in range(len(w)):
                #i 135 w 13 j 0 
                if w[j] not in i:
                    break
                if j+1==len(w):
                    if w in l1: 
                      l1[w]=l1[w]+1
                    else:
                      l1[w]=1 
    
    del c1 # delete the existing candidate set to populate it with new values
    c1={}
    
    for w in l1: # those with minimum support will be eliminated
        if l1[w] > support:
            c1[w]=l1[w]
            
    temp=c1
    c1=l1
    l1=temp        
       
    