# for this assignment not case sensitive for palindromes
#word = input("Enter a word: ")

#def palindrome(word):
    #if word.casefold() == word.casefold()[:: -1]:
       # print(f"{word} is a plaindrome!")
 #   else:
    ##@    print(f"{word} is NOT a palindrome")

#palindrome(word)
new = str()
compare = str()

word =input("Enter a word to see if it is a plaindrome: ")


for each in range(len(word)-1,-1,-1):
    compare += word[each]
    
if compare.lower() == word.lower():
    print(f"{word} is a palindrome. - {word}<--->{compare}")
else:
    print(f"{word} is NOT a palindrome!  - {word}<--->{compare}")
#print(compare)
#print(word)
