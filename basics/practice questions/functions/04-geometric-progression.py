# 4. Implement a function that returns the nth term of the geometric progression.


def geometric_progression(a, r, n):
    return a * (r ** (n - 1))


starting_term = 2
common_ratio = 3
no_of_terms = 4
print(
    f"The {no_of_terms}th term of the geometric progression is: {geometric_progression(starting_term,common_ratio,no_of_terms)}"
)
