def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    values=values
    res=len(values)
    l=[]
    if res==0 or res==1:
        return values
    elif res==2:
        if values[0]>values[1]:
            l.append(values[0])
            l.append(values[1])
            return l
        else:
            return values

    else:
        for i in range(res):
        #    j=i+1
           for j in range(i+1,res):
             if values[i]<values[j]:
               values[i], values[j] = values[j], values[i]
            #   i=j
            #   print(values[i])
            
        
        l.append(values[0])
        l.append(values[1])
        l.append(values[2])
        return l
    pass