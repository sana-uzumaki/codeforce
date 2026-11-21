n = int(input())
win = [()] * n
score = {}
for i in range(n):
    name, point = input().split(" ")
    point = int(point)
    if name in score:
        score[name] += point
    else:
        score[name] = point
    win[i] = (name, score[name])
maxx = max(score.values())
players = []
for i in score:
    if score[i] == maxx:
        players.append(i)
if len(players) == 1:
    print(players[0])
else:
    for name, point in win:
        if point >= maxx and name in players:
            print(name)
            break