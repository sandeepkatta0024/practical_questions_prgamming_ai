#Use map() to add 1 to each element in [5, 10, 15]. [Easy warmup]
numbers=[5, 10, 15]
updated_list=list(map(lambda x: x+1,numbers))
print(updated_list)
print("===================q1 is completed====================")
#Filter numbers divisible by 3 from [1, 2, 3, 4, 6, 9, 12]
numbers=[1, 2, 3, 4, 6, 9, 12]
updated_list=list(filter(lambda x: x%3==0,numbers))
print(updated_list)
print("===================q2 is completed====================")

#Use sorted() with lambda to sort [(1, 'one'), (3, 'three'), (2, 'two')] by the string length.
numbers=[(1, 'one'), (3, 'three'), (2, 'two')]
updated_list=sorted(numbers, key=lambda x:len(x[1]))
print(updated_list)
print("===================q3 is completed====================")
#Map ["apple", "banana"] to their lengths using lambda. Result: [5, 6].
normal_list=["apple", "banana"]
updated_list=list(map(lambda x:len(x),normal_list))
print(updated_list)
print("===================q4 is completed====================")

#Filter dict values > 10 from {"a": 5, "b": 15, "c": 8} using dict.values().
normal_dict={"a": 5, "b": 15, "c": 8}
filtered_dict=dict(filter(lambda x: x[1]>10,normal_dict.items()))
print(filtered_dict)
print("===================q5 is completed====================")
#Use reduce() from functools to sum [1, 2, 3, 4] with lambda (import first)
numbers=[1, 2, 3, 4]
numbers_sum=map(lambda x: x,numbers)
print(numbers_sum)
