n = int(input())
arr = []
score = {"captain":0,"man":1,"woman":2,"child":2,"rat":3}
for i in range(n):
    name, spec = input().split(" ")
    arr.append((name,score[spec]))
arr.sort(key=lambda x: x[1],reverse=True)
for i in arr:
    print(i[0])