#6.5.1.10
word=input("Jakie słowo chcesz znaleść:").upper()
strn=input("Gdzie chcesz szukać Twojego slowa:").upper()


found=True
start=0

for char in word:
    poz=strn.find(char, start)
    if poz<0:
        found=False
        break
    start=poz+1
if found:
    print("YES")
else:
    print("NO")
