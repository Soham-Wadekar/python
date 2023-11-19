# 7. Create a program that searches for a specific pattern in a given string and returns the indices where the pattern is found.

string = "lorem ipsum, dolor sit amet consectetur adipisicing elit. quia perspiciatis minima nisi quod omnis cumque repellat aliquid sit nihil dignissimos."
pattern = "ni"
indices = []

for i in range(len(string) - len(pattern) + 1):
    if string[i: i+len(pattern)] == pattern:
        indices.append(tuple(i+_ for _ in range(len(pattern))))

print(indices)