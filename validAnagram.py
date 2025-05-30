#Better solution
def validAnagram(s,t):
    if(len(s) != len(t)):
        return False
    s,t = list(s),list(t)
    s.sort()
    t.sort()
    sOrdenada = "".join(s)
    tOrdenada = "".join(s)
    if(sOrdenada == tOrdenada):
        return True