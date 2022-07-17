#6.5.1.6
var=int(input("Dekodujesz -> 1 czy szyfrujesz -> 2: "))
text=input("Wpisz tekst:")

shift=0

while shift==0:
    try:
        shift=int(input("Podaj liczbe przesunięć (1-25):"))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift=0
    if shift==0:
        print("Błędna liczba zmian!")
        
ciher=''


for char in text:
    if char.isalpha():
        if var==1:
            code=ord(char)-shift
        elif var==2:
            code=ord(char)+shift
        if char.isupper():
            first=ord('A')
        else:
            first=ord('a')
        code-=first
        code%=26
        ciher+=chr(first+code)
    else:
        ciher+=char
            
print(ciher)

