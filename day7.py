import random

word_list = ["apple","ball","cat","elephant","dog"]

choosen_word = random.choice(word_list)

print(choosen_word)

##Creating blank with underscores
display = ""
for position in range(len(choosen_word)):
    display += " _"
    
print(display)
lives = 6
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter:").lower()
    
    print(guess)
    print(correct_letters)
    display2 =""
    
    for letter in choosen_word:
        if guess == letter:
            display2 += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
             display2 += letter
        else:
            display2 += " _"
            
    if guess not in choosen_word:
        lives -= 1
        if lives ==0:
            game_over = True
            print("You loose game over")
            
            
    
    print(display2)
    
    if "_" not in display2:
        game_over = True
        print("How many lives left:", lives)
        print("You Win.")
print(correct_letters)
