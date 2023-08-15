secret_word = "lesbian"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("bet you don't know my secret word: ")
        guess_count += 1
    else:    
        out_of_guesses = True

if out_of_guesses:
    print("shh you don't know I am a lesbo")
else:
    print("omg you found me out!")