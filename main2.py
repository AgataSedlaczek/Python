x = input ("Podaj swoje imie: ")
print ("Podane przez ciebie imię to", x)
y = (input ("Czy to naprawdę Twoje imię? Odpisz mi: Tak/Nie "))
if y == "Tak":
  print("Bardzo się cieszę, że podałeś prawdziwe imię")
elif y == "Nie":
  print("Bardzo mi przykro, że zostałem oszukany")
else:
  print("Hej, nie odpowiadasz na moje pytanie tak jak proszę!")
