s = 'hell is hello is world good bad hell stay '

l = s.split()

mpp = {}
for s in l:
    if s in mpp:
        mpp[s] += 1
    else:
        mpp[s] = 1
for s in mpp.keys():
    print(s, mpp[s])