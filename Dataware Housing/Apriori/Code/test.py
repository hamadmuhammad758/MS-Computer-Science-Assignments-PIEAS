######################################
def combination(item): 
    outer=inner=0
    final=[]
    for i in item:
        outer+=1
        temp=item[0:outer]
        final.append(i)
        length=len(final)-1
        for j in range(length):
            final.append(final[j]+i)
    return final
###############################3

final=combination("abcde")
count=[]
for i in final:
    count.append(0)
itemsets=["abc","abd","abe","acd","ace","ade","bcd","bce","bde","cde"]
print("**********BRUTE FORCE*****************")
for i in itemsets:
    temp=combination(i)
    for t in temp:
        count[final.index(t)]=count[final.index(t)]+1      
    a=0


support=5 #consider support is 30
support=support/100 *len(final) 
for f in final:
    print(f,count[a])
    a+=1
a=0
print("\nSupport: ",support,"\nFrequent sets","\n")
for f in final:
        if count[a] >= support:
            if(len(f)>1):
                print(f,count[a])
        a+=1
        