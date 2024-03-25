str_manip = input("Enter a sentence: ")
# Calculate and display the length of str_manip
length_str_manip = len(str_manip)
print("Length of the sentence:", length_str_manip)

#Find the last letter in str_manip
last_letter = str_manip[-1]
print("Last letter in the sentence:", last_letter)

# Replace every occurrence of the last letter with '@@
modified_str_manip = str_manip.replace(last_letter, '@')
print("Modified sentence:", modified_str_manip)

last_three_backwards = str_manip[-1:-4:-1]
print("Last three characters of str_manip backwards:", last_three_backwards)

five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word made up of firt three and last two characers:",five_letter_word)