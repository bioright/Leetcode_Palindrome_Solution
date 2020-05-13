# palindrome integer
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.
# Note that this approach is not the best when aiming to save on memory space. but it is the easiest.

def is_palindrome(x):
                                     # first, negative integer cannot be a palindrome by definition
    if x<0:                           # This logic can be skipped because it is implied in step 2.
        print("No")
                                        # 2nd logic is to convert the int to str in order to slice it
    elif str(x)[::-1] == str(x)[0:]:     # compares the reversed str with the original str
        print("Yes")
    else:                                  # for all other cases
        print("No")
is_palindrome(0)                             # put any integer in the function


