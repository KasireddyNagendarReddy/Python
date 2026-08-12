# totalbill caclculation problem
# bill=int(input())
# tip=int(input())
# no_of_people=int(input())
# total_bill=(bill+(tip/100)*bill)/no_of_people
# print(total_bill)


#palindrome or not problem
# def analyze_text(sentence):
#     cleaned_text=sentence.replace(" ","").lower()
#     is_palindrome=cleaned_text==cleaned_text[::-1]
#     if is_palindrome==True:
#         print("it is a palindrome")
#     else:
#         print("not a palindrome")
# analyze_text("race car")



# string formatting problem
# strin="pYtHoN pRoGraMMiNg"
# st1=strin.replace(" ","_").lower().title()
# print(st1)


# prime or not problem
# n=int(input())
# count=0
# if n==2:
#     print("prime")
# elif n<=1:
#     print("not prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")



#bank atm problem
# bank_pin=2006
# acc_bal=45000
# withdr=int(input("enter amount:"))
# attempt=0
# while attempt<3:   
#     u_pin=int(input("enter pin:"))
#     if u_pin==bank_pin:
#         while True:
#             print("\n1. Check Balance")
#             print("2. Withdraw Cash")
#             print("3. Exit")           
#             choice = int(input("Select an option (1-3): "))
#             match choice:
#                 case 1:
#                     print(f"Your current balance is: ₹{acc_bal}")
#                 case 2:               
#                     if withdr<=acc_bal:
#                         print("withdraw successful")
#                     else:
#                         print("no suffiencient funds")
#                 case 3:
#                     print("Thank you for using our ATM. Goodbye!")
#                     break
#         break
#     else:
#         attempt+=1
#         remaining=3-attempt
#         if remaining>0:
#             print("incorrect pin")
#         else:
#             print("account locked")



#Pattern generator problem
# N=int(input("size:"))
# pattern_type=input("enter pattern:")
# if pattern_type=="square":
#     for i in range(N):
#         print("*"*N,sep="")
# elif pattern_type=="triangle":
#     for i in range(1,N+1):
#         print("*"*i)
        
# elif pattern_type=="reverse triangle":
#     for i in range(N,0,-1):
#         print("*"*i)


#remove duplicates problem
# lis=[1, 3, 2, 3, 4, 1, 5]
# new_lis=list(set(lis))
# print(new_lis)

#set operations problem
# python_students = {"Alice", "Bob", "Charlie", "David"}
# java_students = {"Charlie", "David", "Eve", "Frank"}
# print(python_students.intersection(java_students))
# print(python_students.difference(java_students))
# print(python_students.union(java_students))


#word frequency counter 
# para=input("enter a paragraph:")
# new_para=para.replace("!","").replace(" ","")
# dic={}
# for i in new_para:
#     if i in new_para:
#         dic[i]=new_para.count(i)
# print(dic)

#Grade Calculator & Tracker
# students = {"Rahul": [85, 90, 88], "Priya": [92, 95, 91], "Amit": [70, 75, 80]}
# for student,marks in students.items():
#     avg=sum(marks)/len(marks)
#     if avg>=90:
#         print(f"{student}: grade A")
#     elif avg>=80:
#         print(f"{student}: grade B")        
#     else:
#         print(f"{student}: grade C")



# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)   
# print(fibonacci(7))         



# def compress_string(s):
#      count=1
#      for i in range(len(s)):
#           if i < len(s) - 1 and s[i] == s[i+1]:
#                count+=1
#           else:
#                print(s[i] + str(count), end="")
#                count=1  
# compress_string("aaabbbccdaa")  



# def factorial(n):
#     fact=1
#     if n==0 or n==1:     
#         return 1
#     else:
#         for i in range(n,0,-1):
#             fact=fact*i
#         return fact
# print(factorial(5))




# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #[0][0]+[1][1]+[2][2]
# sum=0
# sum2=0
# for i in range(0,len(matrix)):
#         sum=sum+matrix[i][i]
#         sum2=sum2+matrix[i][len(matrix)-1-i]
# print(sum)
# print(sum2)


# store = {"apple": 50, "banana": 20, "milk": 30, "bread": 40}
# cost=0
# cart=[]
# for item,price in store.items():
#     print(f" - {item.capitalize()}: ₹{price}")
# while True:
#     user_input=input("enter item to cart (or 'checkout' to finish):").strip().lower()
#     if user_input=="checkout":
#         break
#     elif user_input in store:
#         cart.append(user_input)
#         print(f"added {user_input}")
#     else:
#         print("item not found")
        
def func1():    
    try:
        l=[1,2,4,5,6]
        i=int(input("enter index:"))
        print(l[i])
        return 1
    except:
        print("error occured")
        return 0
    finally:
        print("end")

x=func1()
print(x)

