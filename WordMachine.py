# Prompts for user input
word = raw_input("Please type a word: ").lower()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

number_list = []
# Converts each letter to alphabet value and appends to number list
for char in word:number_list.append(ord(char) - 96)
# Prints number values of each letter
print("Your word has " + str(len(word)) + " letters. ")
print("The letters in your word are numbered in the alphabet as " + str(number_list))
# Define average value
avg_val = sum(number_list) // len(word)
print("The average value of your word is " + str(avg_val))
print("The letter corresponding to your average value is " + str(alphabet[avg_val - 1


