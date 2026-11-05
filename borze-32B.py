s = input()
code = {"-." : "1", "." : "0", "--" : "2"}
curW = ""
res = ""
for i in s:
    curW += i
    if curW in code:
        res += code[curW]
        curW = ""
print(res)