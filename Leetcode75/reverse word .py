#long way 
        s=s.strip()
        list1=s.split(" ")
        list1=list1[::-1]
        strs=""
        l=list1[len(list1)-1]
        for i in range(len(list1)-1):
            if list1[i] is not "":
                strs=strs+list1[i]+" "
        print(list1) 
        return strs+l  
#in short
return " ".join(reversed(s.split()))
