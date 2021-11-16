# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.



def return_length():
  user_phrase = input("Please enter a word or phrase:")
  length = (len(user_phrase))
  print(f'What you entered is {length} characters long')
  if user_phrase != 'quit':
    return_length()
  else:
    print('goodbye')


return_length()