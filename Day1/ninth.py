def isVowel(p):
    if p in ['a','e','i','o','u']:
        return True
    return False


a = 'KolliVenkataKrishna'

a = a.lower()

mpp = {}

for i in a:
    
    if i in mpp:
        mpp[i]+=1
    else:
        mpp[i] = 1

for i in mpp.keys():
    if(isVowel(i)):
        print(i, mpp[i])