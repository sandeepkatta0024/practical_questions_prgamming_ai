import functools
#Activity 1: Lambda Functions (10 Questions)
# Write lambda to square a number. Use with map() on [1,2,3].
l=[1,2,3]
squared_numbers=list(map(lambda x:x**2, l))
print(squared_numbers)
print("q1 is completed")
# Filter negative numbers from [-1, 2, -3, 4] using lambda + filter().
l=[-1, 2, -3, 4]
negatve_l=list(filter(lambda x:x<0,l))
print(negatve_l)
print("q2 is completed")
#Sort ["cat", "elephant", "dog"] by length using sorted() + lambda.
l=["cat", "elephant", "dog"]
sorted_l=sorted(l,key=lambda x: len(x))
print(sorted_l)
print("q3 is completed")
#use lambda to triple numbers in [5, 10] with map(). Workshop quick practice
l=[5,10]
tripled_l=list(map(lambda x:x*3,l))
print(tripled_l)
print("q4 is completed")
#Chain: Double then filter > 5 from [1, 2, 3, 4].
l=[1, 2, 3, 4]
d_list=list(map(lambda x:x*2,l))
print(d_list)
f_list=list(filter(lambda x:x>5,d_list))
print(f_list)
print("q5 is completed")
#Map two lists [1,2] + [10,20] element-wise using lambda
l1=[1,2]
l2=[10,20]
mapped_l=list(map(lambda x,y: x+y,l1,l2))
print(mapped_l)
print("q6 is completed")

#Filter palindromes from ["radar", "hello", "level"]
l=["radar", "hello", "level"]
filtered_palindromes=list(filter(lambda x:x[::-1]==x,l))
print(filtered_palindromes)
print('q7 is completed')
#Use reduce() to find product of [2, 3, 4]
l=[2, 3, 4]
print(functools.reduce(lambda x,y:x*y,l))
print('q8 is completed')
#Lambda for abs(x) on [-5, 3, -2]
l=[-5, 3, -2]
print(list(map(lambda x:abs(x),l)))
#Sort dict {"a":3, "b":1, "c":2} by values.

dic={"a":3, "b":1, "c":2}
sorted_dic=sorted(dic.items(),key=lambda x:x[1])
print(sorted_dic)