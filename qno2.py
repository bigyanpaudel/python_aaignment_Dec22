# Program to sort alphabetically of words separated by comma.



word = str(input("Enter the word separated by comma : "))



sorted_word = sorted(word.split(','))

final_word = ",".join(sorted_word)



print(final_word)
