array = [3,5,6,7,4,56,76,56,45,34,22,33,9]

for i in array:
  guess_number = int(input("Guess what is the number? : "))
  if i == guess_number:
    print("You guessed it! ")
  else:
    print(" Kepp trying")
