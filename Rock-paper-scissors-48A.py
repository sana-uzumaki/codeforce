fyodor = input()
matroskin = input()
sharic = input()
def pickWin(f, m, s):
    if pick(f, m, s):
        return "F"
    elif pick(m, f, s):
        return "M"
    elif pick(s, f, m):
        return "S"
    return "?"
def pick(f, m, s):
    if f == "rock" and m == "scissors" and s == "scissors":
        return True
    elif f == "scissors" and m == "paper" and s == "paper":
        return True
    elif f == "paper" and m == "rock" and s == "rock":
        return True
    return False
print(pickWin(fyodor, matroskin, sharic))