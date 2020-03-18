
name=input("Enter String To find Frequency :");
temp=""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]} :{name.count(name[i])}")
        temp+=name[i]