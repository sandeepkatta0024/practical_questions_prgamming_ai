#Lambda Functions and Functional Patterns

# See how to define and use simple lambda functions for in-line logic.
# Learn to apply map() and filter() to transform or select data from a list.
# Understand when to use these patterns vs comprehensions.

#q1Write a lambda that takes x and returns x + 10. Assign to add_ten and call with 5.
add_ten=lambda x: x+10
print(add_ten(5))
print("=============================q1 is completed===========================")
#q2 Use map() with lambda to double every number in [1, 2, 3]. Print result.
numbers=[1, 2, 3]
db_every_num=list(map(lambda x: x*2,numbers))
print(db_every_num)
print("=============================q2 is completed===========================")
#q3 Use filter() with lambda to get even numbers from [1, 2, 3, 4, 5]. Print result.

numb=[1, 2, 3, 4, 5]
even_num_list=list(filter(lambda x: x%2==0,numb))
print(even_num_list)
print("=============================q3 is completed===========================")

#create lambda to check if a number > 3. Filter [1, 4, 2, 6] with it.
numb=[1, 4, 2, 6]
filtered_list=list(filter(lambda x: x>3,numb))
print(filtered_list)
print("=============================q4 is completed===========================")

#Use lambda in sorted() to sort ["banana", "apple", "cherry"] by length
unsorted_list=["banana", "apple", "cherry"]
sorted_list=sorted(unsorted_list,key=lambda x:len(x))
print(sorted_list)
print("=============================q5 is completed===========================")
#Use map(lambda x: x.upper(), ["hello", "world"]) and print.
n_list=["hello", "world"]
u_list=list(map(lambda x:x.upper(),n_list))
print(u_list)
print("=============================q6 is completed===========================")
#Filter strings longer than 3 chars from ["hi", "hello", "a", "python"]
n_list=["hi", "hello", "a", "python"]
u_list=list(filter(lambda x:len(x)>3,n_list))
print(u_list)
print("=============================q7 is completed===========================")
#Triple numbers with map() on [10, 20]. Print as list.
numbers=[10,20]
tripled_list=list(map(lambda x:x*3, numbers))
print(tripled_list)
print("=============================q8 is completed===========================")
#Lambda for x * 2 if x > 0 else 0. Map on [-1, 2, -3, 4]
numbers=[-1, 2, -3, 4]
updated_list=list(filter(lambda x: x*2 if x>0 else 0, numbers))
print(updated_list)
print("=============================q9 is completed===========================")
#Get numbers > 5 from [Get numbers > 5 from [3, 7, 2, 8, 1] using filter().
numbers=[3, 7, 2, 8, 1]
filtered_list=list(filter(lambda x:x>5,numbers))
print(filtered_list)