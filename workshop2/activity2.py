# Activity 2: Comprehensions (10 Questions)
# List comprehension: squares of [1,2,3].
# Set comprehension: vowels from "programming". Workshop quick practice
# Dict comprehension: {"a":1, "b":2} → {1:"a", 2:"b"}.
# Filter evens: [x for x in range(10) if x%2==0].
# Flatten [[1,2], [3,4]] → [1,2,3,4].
# Dict: {x: x**2 for x in range(5)}.
# Set: unique chars from "mississippi".
# List: first letters from ["apple", "banana"].
# Conditional: [x*2 for x in range(10) if x>5].
# Nested: [(i,j) for i in [1,2] for j in [3,4]].
l=[1,2,3]
squared_l=[i**2 for i in l]
print(squared_l)
print('q1 is completed')
l="programming"
vowel_l=set(i for i in l if i=='a' or i=='e' or i=='o' or i=='u' or i=='i')
print(vowel_l)
print('q2 is completed')
d={"a":1, "b":2}
updated_d={value:key for key,value in d.items()}
print(updated_d)
print('q3 is completed')
evens_10=list(i for i in range(10) if i%2==0)
print(evens_10)
print('q4 is completed')
l=[[1,2], [3,4]]
# using_lambda=list(map(lambda x,y:x.append(y),l))
print("q5 is not completed")
d={j:j**2 for j in range(1,5)}
print(d)
print("q6 is completed")
s="mississippi"
unq_characters=set(j for j in s)
print(unq_characters)
print("q7 is completed")
l=["apple", "banana"]
first_letters=list(x[0] for x in l)
print(first_letters)
print("q8 is completed")
nums_greater_5=list(x for x in (x*2 for x in range(10)) if x>5)
print(nums_greater_5)