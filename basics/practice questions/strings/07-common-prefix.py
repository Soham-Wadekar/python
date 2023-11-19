# 7. Write a program to find the longest common prefix of a list of strings.

def longest_common_prefix(strings):
    if not strings:
        return ""
    
    strings.sort()

    prefix = ""
    for char1, char2 in zip(strings[0],strings[-1]):
        if char1 == char2:
            prefix += char1
        else:
            break
    
    return prefix

word_list = ['preference', 'prefix', 'premier', 'premium', 'prelude', 'prepare', 'preview', 'preacher', 'prehistoric', 'pregnant']
result = longest_common_prefix(word_list)

print(f"Longest Common Prefix: {result}")