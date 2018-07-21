#regular expressions
#http://www.regex101.com
#^,$,(),{},[],\,?,*,+,.,-
#characterclass==>[]
[iolab]--->b
[a-dp-sA-P0-9z]
# ^acts as negation
[^0-9]
# ^ also acts as beginning of a char class
^[0-9]
# $ is inside the character class it mapps out dollar
# outside the character class shows the end of a char class
# . inside character class means the . itself
# outside character class it means new line
# * and + shows repetition(also known as greedy repetition)
^[ab]*
# * means 0 or more
# + means 1 or more
# ? means 0 or 1
# {m,n} repetation: m-min rep   n-max rep
match password which will contain
1a-z
2A-Z
3.0-9
4ending 'z'
()-used for grouping,has to be excecuted,it means capturing groups
()->storing to memory((2)(3)1) in the order of opening brackets and called  by \1
(?:)-->wont store into memory
roman numerals from 0 to 10
^(i?x|v?i{1,3}|i?v)$
^((i?x|v)|v?i{1,3})$
#[\-]-->
parsing email:
alphanumeric@alphanumeric.com
#-->((^[a-zA-Z0-9,\.]*|[\@])|[a-z,]|([\.]?[a-z]*$))
#-->^[a-zA-Z0-9\-]+@
----------------------------------------=====================================================
looking 
(?=)--> positive look ahead
eg:(?=a)

----==================-------------===================
1 check whether the string entered has minimum 3 digit
^(?=(?:[^0-9]*[0-9]){3})
2. check for password entered
has:
*minimum 1 digit
*minimum 3 CAPS lerrers
*minimum 1 small letter 
*minumum 1 special char
maximu password length 6

====>>>>
^(?=[^0-9]*[0-9])
(?=([A-Z][A-Z]){3})
(?=[^a-z]*[a-z])
(?=[a-zA-Z0-9]*[^a-zA-Z0-9])