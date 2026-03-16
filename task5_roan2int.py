def roman_to_int(s):
    ans=0
    a=list(s)
    print(a)
    dict={ "M":1000,"C":100, "X":10, "I":1,"V":5,"L":50}
    for i in range(1,len(a)):
        if a[i-1] in dict.keys() and a[i] in dict.keys():
            a[i-1]=dict[a[i-1]]  
            a[i]=dict[a[i]]
            if a[i-1]<a[i]:
                val=a[i]-a[i-1]
                ans+=val
                print(f"{ans} in if")
                i+=1
            else:
                ans+=a[i-1]
                print(f"{ans} in else")
    return ans

print(roman_to_int("MCMXCIV"))
