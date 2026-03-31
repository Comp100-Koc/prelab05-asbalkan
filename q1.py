def longest_palindromic_substring(s):
    most=""
    for i in range(len(s)):
        for k in range(i+2,len(s)+1):
            n_letter=s[i:k]
            if n_letter==n_letter[::-1]:
                if len(n_letter)>len(most):
                    most=n_letter
    return most