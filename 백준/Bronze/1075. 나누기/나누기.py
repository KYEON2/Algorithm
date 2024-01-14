n = input()
m = input()

num = int(n[:-2]+'00')

while True:
    if num % int(m) == 0:
        break
    num += 1
    
num = str(num)

print(num[-2:])