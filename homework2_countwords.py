import os.path

if os.path.isfile('./readme.md'):
    with open('./readme.md','rb') as sth:
        list=sth.readlines()
words=0
for lines in list:
    lines=bytes.decode(lines)
    lines=lines.replace(',','')
    lines=lines.strip()
    wo=lines.split(' ')
    words += len(wo)

print(words)



