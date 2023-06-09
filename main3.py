def dodaj(x, y):
  return x+y

def odejmij (x, y):
  return x-y

print("Wybierz operację liczbową:")
print("1.Dodawanie")
print("2.Odejmowanie")

choice=input("Którą operację chcesz wynonac? Wybierz (1/2): ")

num1 = float (input("Podaj pierwszą wartość: "))
num2 = float (input("Podaj drugą wartość: "))

if choice =='1':
  print (num1, "+", num2, "=", dodaj(num1, num2))
elif choice == '2':
  print (num1, "-", num2, "=", odejmij (num1, num2))
else:
  print ("Niepoprawna wartość")

