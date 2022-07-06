def readSubFunc():
    result = ""
    with open("C22BA0.txt", "rt", encoding="utf-8") as ida_asm_file:
        file = ida_asm_file.readlines()
        #print(f"find sub_XXX Function!!!!!!")
        for line in file:
            if line.strip().find('sub_') != -1:
                result += line.strip()
                #print(f"{line.strip()}")
                #print(result)
    return result

def subFuncNotOverlap(): 
    import re
    notOverlap = []
    regex = r" sub_[0-9A-z]{9}"
    matches = re.finditer(regex, readSubFunc(), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        notOverlap.append(match.group().strip())
        #print(f"{match.group().strip()}")

    return set(notOverlap)

def createFridaTestCode():
    subFunc = list(subFuncNotOverlap())
    resultCode = []
    for funcAddreass in subFunc:

        offset = funcAddreass.lstrip("sub_1")
        
        code = 'var module_base = Module.findBaseAddress("PASS");'
        code += f'var custom = module_base.add(0x{offset.lstrip("0")});'
        code += 'Interceptor.replace(custom, new NativeCallback(function() {'
        code += 'console.log();'
        code += f'console.warn("{funcAddreass}");'
        code += 'console.log("-----------------------------------------------------------------------------------");'
        code += '}, "void", []));'
        
        resultCode.append(code)
    
    return resultCode

def saveHookCode():
    fridaHookCode = createFridaTestCode()
    with open("C22BA0.js", "wt", encoding="utf-8") as hookCodeFile:
        for hookCode in fridaHookCode:
            hookCodeFile.writelines(hookCode + "\n")

saveHookCode()