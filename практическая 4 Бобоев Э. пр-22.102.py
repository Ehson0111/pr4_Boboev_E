
#Практическаы 4
"""#Задание 1
file=open("date.txt","w",encoding="utf-8" )

fd=True
while fd==True:
    d=input("Вводите строку ")
    file.write(d+"\n")
    if d==".":
        fd=False
        print("Файл записан")

file.close()

"""
"""#Задание 2
name=input("Введите имя файла ")
with open(name,"r" ,encoding="utf-8") as file:
    sd=file.readlines()

with open(name,"w",encoding="utf-8" ) as file:
    s=1
    for i in sd:
        file.write(f"{s} {i}")
        s+=1
        """
"""#Задание 3 разработать приложение для разделение файла на части приложение принимает на вход имя файла для разделение и целое число
#  n на выходе у приложение  множество файлоов каждый из которых содержит не более чем N строк из исходного файла 
f=input()
N=int(input("Введите N "))
with open(f,"r",encoding="utf-8") as file:
    d=file.readlines()


part=[]                 
n=1
for i in range(0,len(d),N):
    part=d[i:i+N]
    print(part)

    with open(f"{n}.txt", 'w', encoding='utf-8') as part_file:
            part_file.writelines(part)
    n=1+n
"""
"""#задание 4
 
d=input()
s=input()
d1=input("Имя выходного файла ")
with open(d,"r",encoding="utf-8") as file:
    f=file.read()
with open(s,"r",encoding="utf-8") as file:
    f1=file.read()

with open(f"{d1}.txt","a",encoding="utf-8") as file:
    file.write(f)
    file.write(f1)"""
"""#доп1 Разработать приложение которыые выводиьт N Первых строк 
d=input()
N=int(input())
with open(d,"r") as file:
    for i in range(N):
        s=file.readline()
        print(s , end="")

"""
"""#доп2 Разработать приложение которыые выводиьт N последных строк 
d=input("Введите имя файла")
s=True
N=int(input("Введите N "))

with open(d,"r") as file:
    d1=file.readlines()            
d1=d1[-N::]
print(f"{N} конечные строчки файла {d}")

for i in range(len(d1)):
    print(d1[i],end="")"""