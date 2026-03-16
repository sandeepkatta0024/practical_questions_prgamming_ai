import string
#Create a list of 5 fruits. Append "banana", remove "apple", and print the reversed list.
l=["bana","mango","kiwi","qguava","mikk"]
print(l)
l.append("apple")
print(f"after appending the values are {l}")
l.remove("apple")
print(f"after removing the values are {l}")
l.reverse()
print(f"after reversing the values are {l}")

#Given a string s = "hello world", count how many times 'o' appears using s.count().
s="hello world"
count_of_o=s.count("o")
print(count_of_o)
#Write code to compute character frequencies in "mississippi" and store in a dictionary (e.g., {'m':1, 'i':4})
word="mississippi"
d={}
for i in word:
    d[i]=word.count(i)
print(d)
#Convert ["apple", "banana"] to a single string "apple banana" using join().
s=s.join(l)
print(s)
#Create a dictionary person = {"name": "Alice", "age": 25}. Add "city": "Adelaide", then print the keys as a list
person = {"name": "Alice", "age": 25}
person["city"]="Adelaide"
l=list(person.keys())
print(f"the key of person dictionary are {l}")
#Find the most frequent character in "aabbccdd" using a dict and max(). Print char and count.
a="aabbccdd"
d={}
for i in a:
    d[i]=a.count(i)
print(d)
largest=max(d,key=d.get)
largest_char=d[largest]
print(f"largest frequenct is {largest_char} and largest char is {largest}")
#Reverse each string in fruits = ["abc", "def"] to get ["cba", "fed"]. Use list comprehension
fruits = ["abc", "def"]
reversedfruits=[]
for f in fruits:
    reversedfruits.append("".join(reversed(f)))
    
print(reversedfruits)
#Merge d1 = {"a":1, "b":2} and d2 = {"b":3, "c":4} into one dict (d2 overrides). Print result
d1 = {"a":1, "b":2}
d2 = {"b":3, "c":4}
d2.update(d1)
print(d2)
#Check if "python" is substring in "I love python programming". Print positions if found.
s="I love python programming"
s_list=s.find("python")
print(s_list)

#Given text = "aa bb aa cc", split into words, count frequencies with dict, print sorted by count descending.
text="aa bb aa cc"
text_list=text.split(" ")
text_dict={}
for i in text_list:
    if i not in text_dict:
         text_dict[i]=i.count(i)
    else:  
        text_dict[i]=i.count(i)+1
#Extract unique characters from "banana" as a list without duplicates.
text="banana"
listed_txt=list(text)
updated_txt_list=[]
for i in listed_txt:
    if i not in updated_txt_list:
        updated_txt_list.append(i)
print(updated_txt_list)
#Swap first and last elements in lst = [1,2,3,4]. Print new list
lst=[1,2,3,4]
if len(lst)!=0:
    temp=lst[-1]
    lst[-1]=lst[0]
    lst[0]=temp
print(lst)