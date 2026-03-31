def add_binary(a, b):
    a=(a[2:][::-1])
    b=(b[2:][::-1])
    total1=0
    total2=0
    counter=0
    for i in a:
        if i=="1":
            total1+=(2**counter)
        counter+=1
    counter=0
    for k in b:
        if k=="1":
            total2+=(2**counter)
        counter+=1
    result=total1+total2
    kalan=""
    if result==0:
         cevap="0b0" 
    while result>0:
        kalan=str(result%2)+kalan
        result=result//2
    cevap="0b"+kalan
    return cevap
        
        
