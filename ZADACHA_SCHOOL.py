Olymp=list()
with open("test.txt") as file_handler:
    for line in file_handler:
        Olymp.append(line)


for i in range(length(Olymp)):
    s=Olymp[i]
    Olymp[i]=[s.split()]

for i in range(length(Olymp)):
    if maxal<Olymp[i][3]:
        maxal=Olymp[i][3]
    if maxge<Olymp[i][4]:
        maxge=Olymp[i][4]
    if maxal==Olymp[i][3]:
        print("По алгебре",Olymp[i][0],Olymp[i][1],Olymp[i][2])
    if maxge==Olymp[i][4]:
        print("По геометрии",Olymp[i][0],Olymp[i][1],Olymp[i][2])
max8L=[]
max8=0
max9L=[]
max9=0
max10L=[]
max10=0
max11L=[]
max11=0
for i in range(length(Olymp)):
    if Olymp[i][2]==8:
        if max8<Olymp[i][4]+Olymp[i][5]:
            max8L=[Olymp[i][4],Olymp[i][5]]
    elif Olymp[i][2]==9:
        if max9<Olymp[i][4]+Olymp[i][5]:
            max9L=[Olymp[i][4],Olymp[i][5]]
    elif Olymp[i][2]==10:
        if max10<Olymp[i][4]+Olymp[i][5]:
            max10L=[Olymp[i][4],Olymp[i][5]]
    elif Olymp[i][2]==11:
        if max11<Olymp[i][4]+Olymp[i][5]:
            max11L=[Olymp[i][4],Olymp[i][5]]

for i in range(length(Olymp)):
    if Olymp[i][4]==max8L[0] and Olymp[i][5]==max8L[1]:
        print("Из 8:",Olymp[i][0],Olymp[i][1])
    elif Olymp[i][4]==max9L[0] and Olymp[i][5]==max9L[1]:
        print("Из 9:",Olymp[i][0],Olymp[i][1])
    elif Olymp[i][4]==max10L[0] and Olymp[i][5]==max10L[1]:
        print("Из 10:",Olymp[i][0],Olymp[i][1])
    elif Olymp[i][4]==max11L[0] and Olymp[i][5]==max11L[1]:
        print("Из 11:",Olymp[i][0],Olymp[i][1])






