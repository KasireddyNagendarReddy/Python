# n=int(input("enter number:"))
# print("n is greater than 10") if n>10 else print("n is less than 10") if n<10 else print("n is equal to 10")
# #if the given condition is true then it assigns the 9 to x,otherwise 0
# x=9 if n>10 else 0
# print(x)

# a=[1,2,3,4,5,6]
# for index,values in enumerate(a):
#     print(index,values)
#     if index==3:
#         break

n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for name,scores in student_marks.items(): 
    if name==query_name:
        avg_sum=sum(scores)/len(scores) 
print(f"{avg_sum:.2f}")
