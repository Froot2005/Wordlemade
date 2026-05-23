import random
words = ["cats", "rest", "jump", "fire", "moon", "star"]
w = random.choice(words)
attempts=0
while attempts<6:
  guess=input().lower()
  if len(guess)!=4:
    print("Word is too short/long")
    continue
  for i, letter in enumerate(guess):
    if letter==w[i]:
      print("🟢",end="")
    elif letter in w:
      print("🟡",end="")
    else:
      print("⚪",end="")
  print()
  attempts+=1 
  if guess==w:
    print("You win, the word was",w)
    break
else:
  print("You lose, the word was",w)