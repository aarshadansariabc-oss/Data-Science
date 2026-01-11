s = input("Enter here : ")
is_Palindrome = True

left = 0
right = len(s) - 1

while left < right:

    if s[left] != s[right]:
        is_Palindrome = False
        break

    left += 1
    right -= 1

if is_Palindrome:

    print("Its a palindrome")
else:
    print("Its not a palindrome")
