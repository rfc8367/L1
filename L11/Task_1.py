win = int(input("Amount of wins: "))
draw = int(input("Amount of draw: "))
loss = int(input("Amount of loss: "))

def score(win, draw, loss):
    count_points = win * 3 + draw
    return count_points

print(score(win, draw, loss))
