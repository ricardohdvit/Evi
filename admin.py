while True:
    print("1.agregar\n2.borrar\n3.modificar\n4.buscar\n5.mostrar todo\n6.salir")
    op = int(input("que opcion :"))

    if op == 1:
        num = int(input("ingresa la cantidad de computadoras"))
        des = input("ingresa descripcion")
        precio = float(input("precio"))
        ram = input("ram")

        a = open("archivo.txt", "a")
        datos_str = f"{num}|{des}|{precio}|{ram}\n"
        a.write(datos_str)
        a.close()

        print("guardado")

    elif op == 2:
        numero = input("ingresa numero de cumputadora: ") 
        a = open("archivo.txt")
        list_compus = []
        borrado = False
        for fila in a:
            d= fila.strip().split("|")
            if numero == d[0]:
               borrado = True
        else:
            list_compus.append(fila)

        a.close
        if borrado:
            a = open("archivo.txt","w")
            for c in list_compus:
                a.write(c)
            a.close()
        else:
            print("numero no encontrado")
    
    elif op == 3:
        numero = input("ingresa numero de cumputadora: ") 
        a = open("archivo.txt")
        list_compus = []
        modificado = False

        for fila in a:
            d= fila.strip().split("|")
            if numero == d[0]:
                modificado = True

                des = input("ingresa nueva descripcion")
                precio = float(input(" nuevo precio"))
                ram = input("nuevo ram")
                datos_nuevod_str = f"{num}|{des}|{precio}|{ram}\n"
                list_compus.append(datos_nuevod_str)
        else:
            list_compus.append(fila)

        a.close
        if modificado:
            a = open("archivo.txt","w")
            for c in list_compus:
                a.write(c)
            a.close()
        else:
            print("numero no encontrado")
    elif op == 4:
        numero = input("ingresa numero de cumputadora") 
        a = open("archivo.txt")
        for fila in a:
            d= fila.strip().split("|")
            if numero == d[0]:
                print(f"{num}|{des}|{precio}|{ram}\n")
                print(f"{d[0]:<5}{d[1]:<25}{d[2]:<10}{d[3]:<10}")
                break
        else:
            print("error")
        a.close

    elif op == 5:
        print("registro de computadores")
        print(f"{'num':<5}")
        a = open("archivo.txt")

        for fila in a :
            d = fila.strip().split("|")
           
    elif op == 6:
        break