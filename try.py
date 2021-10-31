a = [' ', ' ', 'O']
b = [' ', 'O', 'O']
c = ['O', 'O', 'O']

all = a+b+c
target = [j for j in range(9) if all[j] == "O"]
win_pattern = [[0,1,2],[3,4,5],[6,7,8]]
pattern = [6,7,8]
print(all)
print(target)
print(target in win_pattern)
print(target in pattern)