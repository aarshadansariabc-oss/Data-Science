# Palindrome

word = 'racecar'
is_palindrome = True
left = 0
right = len(word) - 1

while left < right:
    if word[left] != word[right]:
        is_palindrome = False

    left += 1
    right -= 1

if is_palindrome:
    print("Its a palindrome")
else:
    print("Not a palindrome")
