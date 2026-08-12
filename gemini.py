# n=input("enter an alphabet:").lower()
# match n:
#     case 'a'|'e'|'i'|'o'|'u':
#         print("n is vowel")
#     case _:
#         print("n is consonant")
    
n=int(input("enter the value of n:"))
count=1

for i in range(1,n+1):
    count=count*i
print(count)