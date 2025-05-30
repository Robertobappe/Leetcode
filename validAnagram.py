def validAnagram(s,t):
    if(len(s) != len(t)):
        return False
    s.sor()
    print(s)
    return None

print(validAnagram('anagram','nagaram'))