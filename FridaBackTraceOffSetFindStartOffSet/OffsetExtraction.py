
def readFile():
    with open("test.log", "rt") as FridaBackTraceOffsetFile:
        BackTraceOffsetResult = []
        FridaBackTraceOffset = FridaBackTraceOffsetFile.readlines()

        for BackTraceOffset in FridaBackTraceOffset:
            BackTraceOffsetResult.append(BackTraceOffset.strip())
    
    return BackTraceOffsetResult

def findBinaryOffset():
    import re

    IDAOffset = []
    file = readFile()
    binaryRegex = r"^0x[0-9A-Fa-f]{9} TAuth!0x[0-9A-Fa-f]{6} \(0x[0-9A-Fa-f]{9}\)"
    IDAOffsetRegex = r"^0x[0-9A-Fa-f]{9} TAuth!0x[0-9A-Fa-f]{6} "

    for offset in file:
        matches = re.finditer(binaryRegex, offset, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            #print(re.sub(IDAOffsetRegex, "", match.group()))
            IDAOffset.append(re.sub(IDAOffsetRegex, "", match.group()))
    
    return list(set(IDAOffset))
            

def MakeIDAOffSet():
    BinaryOffset = findBinaryOffset()
    IDAOffSet = []

    for offset in BinaryOffset:
        IDAOffSet.append(offset[1:-1])

    return IDAOffSet

def SaveOffSetFile():
    import os
    DesktopPath = os.path.join(os.path.expanduser('~'),'Desktop') + "\\" + "IDAOffSet.txt"
    IDAOffSet = MakeIDAOffSet()

    with open(DesktopPath, "wt") as IDAOffSetFile:
        for OffSet in IDAOffSet:
            #print(OffSet)
            IDAOffSetFile.write(OffSet.upper() + "\n")

SaveOffSetFile()