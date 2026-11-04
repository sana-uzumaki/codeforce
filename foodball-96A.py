# s = input()
# curW = 1
# for i in range(1,len(s)):
#     if s[i] == s[i-1]:
#         curW += 1
#     else:
#         curW = 1
#     if curW >= 7:
#         print("YES")
#         break
# else:
#     print("NO")
s = input()
last = s[0]
flag = True
curW = 0
for i in s:
    if i != last:
        last = i
        curW = 1
    else:
        curW += 1
    if curW >= 7:
        flag = False
        break
print("NO" if flag else "YES")