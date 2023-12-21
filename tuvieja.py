print("Elige qué cambio hacer:")
print("\n1. Celsius a Fahrenheit")
print("\n2. Fahrenheit a Celsius")
print("\n3. Celsius a Kelvin")
print("\n4. Kelvin a Celsius")
print("\n ")
Formula = int(input())

if Formula == 1:
  c = int(input("grados Celsius "))
elif Formula == 2:
  f = int(input("grados Fahrenheit "))
elif Formula == 3:
  c2 = int(input("Grados Celsius "))
else:
  k = int(input("Grados Kelvin"))

#division  del papuh

if Formula == 1:
  F = c * 1.8 + 32.
  print("\n", c,"Grados Celsius son",F, "Fahrenheit")
elif Formula == 2:
  C = (f - 32) / 1.8
  print("\n", f, "Grados Fahrenheit son", C, "Celsius")
elif Formula == 3:
  K = c2 + 273.15
  print("\n", c2, "Grados Celsius son",K, "Kelvin")
else:
  C = -273.15 * k
  print("\n", k,"Grados Kelvin son", C, "Celsius")


