with open("sample2.txt",'r') as source:
    content = source.read()
with open("sample.txt",'w') as destination:
    destination.write(content)

print('Success')