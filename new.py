i = 0
while i < 5:
    print(i)
    i += 1

secret = "ricky"
guess = ""
count = 0
limit = 3
out_of_guesses = False

while guess != secret and not(out_of_guesses):
    if count <limit:
        guess = input("Enter guess: ")
        count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose")
else:
    print("You win")