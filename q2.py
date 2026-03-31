def remove_adjacent_duplicates(s):
    count=0
    new=s
    while count<(len(new)-1):
        if new[count]==new[count+1]:
           new=new[0:count]+new[count+2:(len(new)+1)]
           count=0
        else: 
            count+=1
    return new
    
                    
print(remove_adjacent_duplicates("abbacadd"))