# 1.Tab \t Adds space.
# 2.New line \n Adds new line.
# 3. Backslash \\ Adds a backslash.
# 4. Single quote \' Adds a single quote.
# 5. Double quote \" Adds a double quote.
# 6. Curly braces {{ or }} Adds a curly brace.
# 7.Backspace \b Removes previous character.
# 8.Raw Strings (r) Ignores escape characters.
# 9. Unicode \u Adds a unicode character.
name='ram'
age=16
city='ktm'
print('my name is {0} and age is {1}'.format(name,age))
# resuing the variable by using index 
print ('my name is {0} and {0} lives in {2} and age of {1}'.format(name,age,city))

# using f-strings
print(f"My name is {name} and age is {age}")

print(f"My name is {name} and {name} is {age} years old who lives in {city}")
#f-string is usually preferred because it is shorter and easier to read.