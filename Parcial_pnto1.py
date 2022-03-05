import msvcrt

#Punto 1 by JeisonGarzon

n = 1
while n == 1:
    op = int(input("¿Que desea hacer? \n 1 -> Modificar\n 2 -> Buscar\n 3 -> Reemplazar\n 4 -> Dividir\n 5 -> salir\n  Su opción: "))
    txt0 = ("Ha seleccionado")
    counter = 0
    counter1 = 0
    if op == 1:
        print(txt0," modificar texto")
        txt1 = str(input("Introduzca el texto a continuación: "))
        
        op1 = int(input("¿Que desea hacer? \n1-- Eliminar todas x letras\n2--Pasarlo todo a Mayus/Minus\n3--Contar letras\n "))
        if op1 == 1:
            print("Eliminar una letra de todo el texto")
            op2 = str(input("\n ¿Que letra desea eliminar? "))
            
            for x in txt1:
                if x == op2:
                    txt1 = txt1.replace(x,"")
            print(txt1)
            
            
        elif op1 == 2:
            print("Formatear texto a mayuscula o minuscula")
            
            op2 = int(input("\n 1 -- Mayuscula\n 2 -- Minuscula"))
            
            if op2 == 1:
                txt1 = txt1.upper()
            elif op2 == 2:
                txt1 = txt1.lower()
                
            print(txt1)
            
            
        elif op1 == 3:
            print("Contar los caracteres del texto \n")
            
            for x in txt1:
                if x in txt1:
                    counter = counter+1
                    if x == " ":
                        counter1 = counter1 +1
            print("Numero de caracteres con espacios: ",counter)
            counter = counter-counter1
            print("Numero de caracteres sin espacios: ",counter)
            
            
        else:
            print("Opcion invalida")
            
            
    elif op == 2:
        print(txt0," buscar texto")
        txt1 = str(input("Introduzca el texto a continuación: "))
        op1 = str(input("Introduzca la palabra o frase que desea buscar en texto: "))
        
       
        counter = txt1.count(op1)
        
        if op1 in txt1:
            print("La entrada ",op1," se encuentra en el texto ",counter," veces")
        else:
            print("La entrada ",op1," no se encuentra en el texto. ")
        
    elif op == 3:
        print(txt0," reemplazar texto")
        txt1 = str(input("Introduzca el texto a continuación: "))
        op1 = str(input("Introduzca la palabra o frase que desea reemplazar en el texto: "))
        op2 = str(input("Introduzca la nueva palabra que quiere introducir en texto: "))
        
        txt1 = txt1.replace(op1,op2)
        print(txt1)
        
    elif op == 4:
        print(txt0," dividir palabras")
        txt1 = str(input("Introduzca el texto a continuación: "))
        
        lista = txt1.split()
        lista1 = []
        for x in txt1:
            lista1.append(x)
        
        print("Separada por palabras: ",lista,"\nSeparada por letras: ",lista1)
        
    elif op == 5:
        print("\nHasta la proxima")
        n = 0
    else:
        print("Opcion invalida")
    
    
    msvcrt.getch()