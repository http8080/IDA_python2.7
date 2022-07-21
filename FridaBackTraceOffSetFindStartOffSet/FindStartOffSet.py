from idc_bc695 import PrevFunction, NextFunction
import os

def readFridaOffSetFile():
    DesktopPath = os.path.join(os.path.expanduser('~'),'Desktop') + "\\" + "IDAOffSet.txt"
    OffSet = []

    with open(DesktopPath, "rt") as FridaOffSetFile:
        OffSetFile = FridaOffSetFile.readlines()

        for FridaOffSet in OffSetFile:
            OffSet.append(FridaOffSet.strip())

    return OffSet

# NextFunction(PrevFunction(4308426448))
def hexToInt():
    HexOffSet = readFridaOffSetFile()
    intOffSet = []

    for OffSet in HexOffSet:
        intOffSet.append(int(OffSet[2:], 16))
        # print(int(OffSet[2:], 16))

    return intOffSet

def findStartOffset():
    intOffSet = hexToInt()
    StartOffSet = []

    for OffSet in intOffSet:
        StartOffSet.append(NextFunction(PrevFunction(OffSet)))
    
    return StartOffSet

def intToHex():
    StartOffSet = findStartOffset()
    HexStartOffSet = []

    for OffSet in StartOffSet:
        HexStartOffSet.append(hex(OffSet))

    return HexStartOffSet

def SaveHexStartOffSet():
    DesktopPath = os.path.join(os.path.expanduser('~'),'Desktop') + "\\" + "ResultStartOffSet.txt"
    HexStartOffSet = intToHex()
    

    with open(DesktopPath, "wt") as StartOffSetFile:       
        for StartOffSet in HexStartOffSet:
            StartOffSetFile.writelines(StartOffSet[:-1] + "\n")

SaveHexStartOffSet()