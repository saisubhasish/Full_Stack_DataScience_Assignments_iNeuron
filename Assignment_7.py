
# 1. The feature responsible for generating Regex objects is re.compile().
#    Because of Regex object search operation became easy and we do perform it through a search pattern.


# 2. Raw strings are appeared in Regex objects so that backslashes do not have to be escaped.
#    Raw string with backslashes give some extra functionality.


# 3. Search() method returns the index of the matched element, or -1 if no element matched.


# 4. From a Match item, how do you get the actual strings that match the pattern?
# Step 1 - Need to import re module
# Step 2 - Create a Regex object with the re.compile() function.
# Step 3 - Pass the string from where you want to search the Regex object by using search() function. This statement
#          returns a match object.
# Step 4 - Call the match object's group() method to return the actual matched text.


# 5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', Group 0 covers entire match result, group 1
#    covers the first set of parentheses, and group 2 covers the second set of parentheses.


# 6. In standard expression syntax, parentheses and intervals have distinct meanings. You can get a regex if you want
#    it to fit real Periods and parentheses as it can be escaped with a backslash: \., \(, and \).


# 7. The findall() method returns a string list or a list of string tuples. It'll return one of the two options if the
#    regex has no groups, list of strings is returned. If the regex has groups, list of tuples of strings is returned.


# 8. In standard expressions, the | character signifies matching “either, or” between two groups.


# 9. Character not mentioned.


# 10. In regular expressions, the + matches one or more. The * matches zero or more.


# 11. In regular expression the {4} matches exactly three instances of the preceding group. The {4,5} matches between
#     four and five instances.


# 12. In regular expressions the \d, \w, and \s shorthand character classes match a single digit, word, or space
#     character, respectively.


# 13. The \D, \W, and \S shorthand character classes match a single character that is not a digit, word, or space
#     character, respectively.


# 14. The .* performs a greedy match, and the .*? performs a nongreedy match.


# 15. The syntax for matching both numbers and lowercase letters with a character class is Either [0-9a-z] or [a-z0-9]


# 16. The procedure for making a normal expression in regax case insensitive is by  passing re.I or re.IGNORECASE as
#     the second argument to re.compile() will make the matching case insensitive.


# 17. The .character normally matches any character except the newline character. If re.DOTALL is passed as the second
#     argument to re.compile(), then the dot will also match newline characters.


# 18. If numReg = re.compile(r'\d+'), the return of numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') will
#     be 'X drummers, X pipers, five rings, X hens'


# 19. The re.VERBOSE passing as the 2nd argument to re.compile() allows you to add whitespace and comments to the
#     string passed to re.compile()


# 20. A regex that match a number with comma for every three digits and match the following is :
#     e.compile(r'^\d{1,3}(,{3})*$')
#
#     '42'
#     '1,234'
#     '6,368,745'
#     but not the following:
#     '12,34,567' (which has only two digits between the commas)
#     '1234' (which lacks commas)


# 21. A regex that matches the full name of someone whose last name is Watanabe, the first name that comes before it
#     will always be one word that begins with a capital letter. And the regex match the following is :
#     re.compile(r'[A-Z][a-z]*\sWatanabe')
#
#     'Haruto Watanabe'
#     'Alice Watanabe'
#     'RoboCop Watanabe'
#      but not the following:
#     'haruto Watanabe' (where the first name is not capitalized)
#     'Mr. Watanabe' (where the preceding word has a nonletter character)
#     'Watanabe' (which has no first name)
#     'Haruto watanabe' (where Watanabe is not capitalized)


# 22. A regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either
#     eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period, This
#     regex should be case-insensitive and match the following is :
#     re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\ s(apples|cats|baseballs)\.', re.IGNORECASE)
#
#     'Alice eats apples.'
#     'Bob pets cats.'
#     'Carol throws baseballs.'
#     'Alice throws Apples.'
#     'BOB EATS CATS.'
#     but not the following:
#     'RoboCop eats apples.'
#     'ALICE THROWS FOOTBALLS.'
#     'Carol eats 7 cats.'



import re

text = 'Sai Subhasish Rout'
result  = re.search("^Sai.*Rout$",text)

if result:
    print('Successfully matched')
else:
    print('Not get the match')
