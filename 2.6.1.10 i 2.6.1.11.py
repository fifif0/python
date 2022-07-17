#2.6.1.10
print("2.6.1.10\n")
x = float(input("Enter value for x: "))
y=1/(x+1/(x+1/(x+(1/x))))
print("y =", y)
print("\n")
#2.6.1.11
print("2.6.1.11\n")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins_=(mins+dura)%60
hour_= int(hour + (mins + dura)/60)%24
print(hour_,":",mins_)
print("\n")
#LOKATA
print("LOKATA\n")
opro=1.5
print("Oprocentowanie nalezy ustalic jako",opro,"% w skali rok.")
czas_trwania = int(input("podaj czas trwania lokaty (w latach): "))
wklad_wlasny = int(input("Podaj wartość wpłaconych pieniędzy: "))
wynik=wklad_wlasny*(1+opro*(1/100))**czas_trwania
print("Twoje saldo będzie wynosić:",round(wynik,3),"PLN")
print("Twój zysk to:",round(round(wynik,3)-wklad_wlasny,3),"PLN")
