import os

def readFridaOffSetFile():
    DesktopPath = os.path.join(os.path.expanduser('~'),'Desktop') + "\\" + "ResultStartOffSet.txt"
    OffSet = []

    with open(DesktopPath, "rt") as FridaOffSetFile:
        OffSetFile = FridaOffSetFile.readlines()

        for FridaOffSet in OffSetFile:
            OffSet.append(FridaOffSet.strip())

    return OffSet


def createFridaTestCode():
    subFunc = list(readFridaOffSetFile())
    resultCode = []

    for funcAddreass in subFunc:
        offset = funcAddreass.lstrip("0x1")
        offset = offset.lstrip("0")
        
        code = 'var module_base = Module.findBaseAddress("TAuth");'
        code += f'var custom = module_base.add(0x{offset.lstrip("0")});'
        code += 'Interceptor.replace(custom, new NativeCallback(function() {'
        code += 'console.log();'
        code += f'console.warn("sub_{funcAddreass[2:]}");'
        code += 'console.log("-----------------------------------------------------------------------------------");'
        code += '}, "void", []));'
        
        resultCode.append(code)
    
    return resultCode

def saveHookCode():
    DesktopPath = os.path.join(os.path.expanduser('~'),'Desktop') + "\\" + "StartOffSetHook.js"
    fridaHookCode = createFridaTestCode()
    with open(DesktopPath, "wt", encoding="utf-8") as hookCodeFile:
        for hookCode in fridaHookCode:
            hookCodeFile.writelines(hookCode + "\n")

saveHookCode()