# 5. Implement a function to check if a list is a palindrome.


def check_list_palidrome(lst):
    if lst == list(reversed(lst)):
        print(f"The list {lst} is a palindrome")
    else:
        print(f"The list {lst} is not a palindrome")


check_list_palidrome([1, 2, 3, 2, 1])
check_list_palidrome([1, 2, 3])

## ONE LINE

print(
    "Palindrome"
    if [1, 2, 3, 2, 1] == list(reversed([1, 2, 3, 2, 1]))
    else "Not Palindrome"
)
