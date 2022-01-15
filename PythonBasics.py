'''
#1
a = str(input())
print(a[-1] + a[1: len(a)-1] + a[0])

# 2
a = int(input())
ans = 1
if a == 0:
	print(1)
else:
	while a > 0 :
		ans *= a
		a -= 1
	print(ans)
'''

# 3
from random import randint

 
def f(Man, Bot):
	mw = "You won"
	bw = "You lose"
	if Man == Bot:
		return ("Draw")
	elif (Man == 0 and Bot == 1) or (Man == 1 and Bot == 2) or (Man == 2 and Bot == 0):
		return(mw)		

	else:
		return(bw)


main = ['rock', 'scissors', 'paper']

HumWord = str(input("rock, scissors, paper? \n"))
HumMove = main.index(HumWord)

BotMove = randint(0, 2)
BotWord = main[BotMove]

print("Bot's move - ", BotWord, "\n", f(HumMove, BotMove))
