dic1={"chef":"vamshi","waiter":"nani"}
# print(dic["chef"])
# dic["accountant"]="rahul"
# print(dic)
# print(dic.get("clean"))
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# dic.update({"chef":"sai"})
# print(dic)
dic2={"manager":"sweety","cleaner":"mani"}
dic1.update(dic2)
print(dic1)
dic1.pop("nani")
print(dic1)