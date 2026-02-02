#generate all subsequences in both
#can reduce the correct cases by ignoring letters which do not appear in both
#order does not matter, keep dictionaries instead

def string_permutation(s1,s2):
    valid_letters=set(s1).intersection(set(s2))
    s1_freqs=dict.fromkeys(valid_letters,0)
    s2_freqs=dict.fromkeys(valid_letters,0)
    for i in s1:
        if i in valid_letters:
            s1_freqs[i]+=1
    for i in s2:
        if i in valid_letters:
            s2_freqs[i]+=1
    a=""
    for i in valid_letters:
        val=min(s1_freqs[i],s2_freqs[i])
        if val!=0:
            a+= i*val
    return a
    
    
        

print(string_permutation("horses","ores"))
print(string_permutation("subsequence","seated"))
