string = input()

player_1, player_2 = 0, 0

for i in range(len(string)):
    if not string[i].isalpha():
        continue
    elif string[i].lower() in "aeiou":
        player_2 += len(string)-i
    else:
        player_1 += len(string)-i

if(player_1> player_2):
    print("Stuart",player_1)
elif(player_1< player_2):
    print("Kevin", player_2)
else:
    print("Draw")
