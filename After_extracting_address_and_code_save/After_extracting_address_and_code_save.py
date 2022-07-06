#현재 함수 디스어셈블 출력 및 저장
# 함수가 너무 커서 출력 못할때....
# python2

ea = here()

start = GetFunctionAttr(ea, FUNCATTR_START)

end = GetFunctionAttr(ea, FUNCATTR_END)

cur_addr = start

myfile = open("C:\\Users\\http80\\Desktop\\C22BA0.txt", 'w')

while cur_addr <= end:

    print hex(cur_addr), GetDisasm(cur_addr)
    myfile.write(hex(cur_addr) + "\t" + GetDisasm(cur_addr) + '\n')
    cur_addr = NextHead(cur_addr, end)
    
myfile.close()