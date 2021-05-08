stop = False
init = True
update = False
fail = True
tB = 400
tE = 1800
inA = 0
inB = 0
length = 0
tempA = 0
tempB = 0
apoList = [0, 0]
while stop is False:
    if init is True:
        # Server Var Init
        inA = 410
        inB = 420
        length = 2
        tempA = 0
        tempB = 0
        apoList = [0, 0, 500, 560]
        # Boolean Init
        init = False
        update = False
        fail = True
    while update is True:
        update = False
        if tB < inA < tE:
            if tB < inB < tE:
                fail = False
                while length > -1:
                    tempB = (apoList[length-1])
                    length -= 1
                    tempA = (apoList[length-1])
                    if inA < tempA and inB < tempA:
                        pass
                    elif inA > tempB and inB > tempB:
                        pass
                    else:
                        fail = True
                    if fail is True:
                        length = -1
    if fail is False:
        init = True
        apoList.append(inA)
        apoList.append(inB)
