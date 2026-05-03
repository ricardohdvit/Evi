class Mi_clase:
   def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

   def sumar(self):
        return self.num1 + self.num2 + self.num3

   def mayor(self):
         return max(self.num1, self.num2, self.num3)

   def menor(self):
         return min(self.num1, self.num2, self.num3)

   def iguales(self):
         return self.num1 == self.num2 == self.num3

   def concatenar(self):
         return str(self.num1) + str(self.num2) + str(self.num3)
         
print("Que numeros quieres utilizar")
num1 = int(input("Primer numero :"))
num2 = int(input("Segundo numero :"))
num3 = int(input("Tercer numero :"))

objeto = Mi_clase(num1,num2,num3)

while True:
   print("Que operacion quieres elegir ")
   print("\n1.Sumar\n2.Mayor\n3.Menor\n4.Iguales\n5.Concatenar\n6.Salir")
   op = input("Opción: ")

   if op == "1":
      print(f"{objeto.sumar()}")
   elif op == "2":
      print(f"{objeto.mayor()}")
   elif op == "3":
      print(f"{objeto.menor()}")
   elif op == "4":
      print(f"{objeto.iguales()}")
   elif op == "5":
      print(f"{objeto.concatenar()}")
   elif op == "6":
      break
   else:
      print("Error")