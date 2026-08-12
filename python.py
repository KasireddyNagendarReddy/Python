# # name="Nani"
# # print(name.upper())
# # print(name.lower())
# # print(name)
# # print(name.rstrip("i"))

# blog="hi my name is Nani"
# # print(blog.capitalize())
# # print(blog.title())
# # print(blog.split(" "))
# # print(blog.split("m"))
# # print(len(blog))
# # print(len(blog.center(20,"!")))
# print(blog.endswith("i",1,12))
# print(blog.isalpha())
# import time 

# timestamp=time.strftime('%H:%M:%S')
# print(timestamp)

# timestamp1=int(time.strftime("%H"))
# print(timestamp1)

# timestamp=int(time.strftime("%M"))
# print(timestamp)

# timestamp=int(time.strftime("%S"))
# print(timestamp)

# if 4<timestamp1<12:
#     print("good morning")
# elif 12<timestamp1<16:
#     print("good afternoon")
# elif 16<timestamp1<20:  
#     print("good evening")

x=int(input("emter the value of x:"))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case _ if x>2:
        print("x is not within the range")