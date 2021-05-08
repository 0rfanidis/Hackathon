f = open("sched.txt", "r")
tempList = f.readlines()
apoList = []
for element in tempList:
    apoList.append(element.strip())
apoList = list(map(int, apoList))
fail = False
tB = 400
tE = 1800
inA = 1100
inB = 1101
length = len(apoList)
tempA = 0
tempB = 0
if tB < inA < tE:
    if tB < inB < tE:
        while length > 1:
            tempB = (apoList[length-1])
            length -= 1
            tempA = (apoList[length-1])
            length -= 1
            if inA < tempA and inB < tempA:
                pass
            elif inA > tempB and inB > tempB:
                pass
            else:
                fail = True
            if fail is True:
                length = 1
                print("fail")
    else:
        fail = True
else:
    fail = True
if fail is False:
    f.close()
    f = open("sched.txt", "a")
    f.write(str(inA) + "\n")
    f.write(str(inB) + "\n")
    print("success")
    exit(0)
