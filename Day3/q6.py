# sentence = "the quick brown fox jumps over the lazy dog"

# mpp = {}

# for s in sentence.split():
#     if s in mpp:
#         mpp[s]+=1
#     else:
#         mpp[s] = 1

# ans = {s:mpp.get(s) for s in mpp.keys()}

# print(ans)

sentence = "the quick brown fox jumps over the lazy dog"

ans = {word:sentence.split().count(word) for word in dict.fromkeys(sentence.split())}

print(ans)