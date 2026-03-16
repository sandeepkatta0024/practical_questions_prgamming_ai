# import string
# def rle_encode(s):
#     s=list(s)
#     a=[]
#     for i in range(len(s)):
#         if s[i] in list(string.digits):
#             if not i==0:
#                 a+=s[i-1]*s[i]
#     return a

    

# def rle_decode(t):
#     pass

# print(rle_encode("aaab3sn2s"))
# print(rle_decode("a2m3nw22"))

def rle_encode(s: str) -> str:
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result


def rle_decode(t: str) -> str:
    result = ""
    i = 0

    while i < len(t):
        char = t[i]
        i += 1

        num = ""
        while i < len(t) and t[i].isdigit():
            num += t[i]
            i += 1

        result += char * int(num)

    return result


# Example
print(rle_encode("aaabbc"))   # a3b2c1
print(rle_decode("a3b2c1"))   # aaabbc