from random import randrange

def computer_play():
  options = ['rock','paper','scissors']
  return(options[randrange(3)])

no_of_plays = int(input("Enter how many games would you like to play in best of :"))
winning_game = 0

for i in range(no_of_plays):
  user_option = input(f"Game {i+1}: Enter whether you like to play rock, paper or scissors ")
  computer_choice = computer_play()
  print(f"Your {user_option} -vs- Computer's {computer_choice}")
  if user_option == computer_choice:
    winning_game += 1

if(winning_game > (no_of_plays/2)):
  print(f"You have won ! You: {winning_game} | Computer: {no_of_plays-winning_game}")
elif(winning_game == (no_of_plays/2)):
  print(f"Played well but tie occurs ! You: {winning_game} | Computer: {no_of_plays-winning_game}")
else:
  print(f"You lost the game ! You: {winning_game} | Computer: {no_of_plays-winning_game}")


