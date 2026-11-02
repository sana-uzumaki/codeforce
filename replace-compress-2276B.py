# brute force code 

# n = int(input())
# def compress(passS):
#     comprS = f"{passS[0]}"
#     for i in passS:
#         if comprS[-1] != i:
#             comprS += i
#     return comprS
# while n > 0:
#     n -= 1
#     s = input()
#     size = len(s)
#     res = set()
#     res.add(compress(s))
#     for i in range(1,size-1):
#         if s[i-1] == s[i+1]:
#             curW = s[:i] + f"{"0" if s[i] == "1" else "1"}" + s[i+1:]
#             res.add(compress(curW))
#     print(len(res))

n = int(input())
while n > 0:
    n -= 1
    s = input()
    size = len(s)
    midSame = 0
    midDiff = 0
    for i in range(1,size - 1):
        if s[i-1] == s[i+1]:
            if s[i] == s[i+1]:
                midSame = 1
            else:
                midDiff = 1
        if (midDiff + midSame) == 2:
            break
    print(1 + midDiff + midSame)