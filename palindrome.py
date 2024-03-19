# using for two pointer method( left,right)

# num = int(input("Enter the numbers : "))
# def ispalindrome(num):
    
#     string = str(num)
    
#     left = 0
    
#     right = len(string) - 1
    
#     while left <= right:
        
#         if int(string[left])==int(string[right]):
#             left+=1
#             right-=1
#         else:
#             return False
#     return True

# print(ispalindrome(num))


#for word

# word = str(input("Enter the word : "))

# def ispalindrome(word):
    
#     word_lower = word.lower()
    
#     left = 0
    
#     right = len(word_lower) - 1
    
#     while left <= right:
        
#         if word_lower[left]==word_lower[right]:
#             left+=1
#             right-=1
#         else:
#             return False
#     return True

# print(ispalindrome(word))


# str1 = input('enter the str: ')
# str1 = str1.replace('"', '')
# x= list(map(int,str1.split()))

# string2 = x[0]/x[1]
# print(string2)

# str1 = input('enter the str: ')
# str1 = str1.replace('"', '#')
# print(str1)

# x = int(input("enter the num: "))

# n = str(x).replace('','"')
# n.split(',')
# print(n)

# x = int(input("enter the num: "))

# n = ','.join(['"' + digit + '"' for digit in str(x)])
# print(n)

# Get input from the user
# x = int(input("enter the num: "))

# # Convert the integer input into a string and iterate over each digit
# digits_with_quotes = []
# for digit in str(x):
#     # Surround each digit with double quotes and append it to the list
#     digits_with_quotes.append('"' + digit + '"')
    
# print(digits_with_quotes)

# # Join the list elements with commas to form the final string
# n = ','.join(digits_with_quotes)

# # Print the final string
# print(type(n))









# x = int(input("enter the num: "))

# n = '"' + '" "'.join(str(x)) + '"'
# n = n.replace('""', '", "')
# print(n)

# y = list(map(str,x))

# print(y)
