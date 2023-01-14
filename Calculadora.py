#Calculadora 
import math   
#import numpy as np 
 
 
print('Programa Práctica Calculadora') 
 
opc_operacion = 0 
 
while True: 
    print( """ 
     
        Selecciona la operación que quieres ejecutar:  
 
    [1] Suma  
    [2] Resta 
    [3] Multiplación 
    [4] División 
    [5] Raíz Cuadrada 
    [6] Exponente n 
    [7] Seno 
    [8] Coseno 
    [9] Tangente 
    [10] Cerrar Calculadora 
    """ 
    ) 
 
    #Declaración de variables 
    try: 
        opc_operacion = int (input ('Operación: ')) 
        operacion = int 
        val1 = float 
        val2 = float 
        resultado=float 
        valgrados = int 
         
        #funcion operación  
        def func_operacion(opc_operacion): 
         if opc_operacion == 5: 
                val1rc = float (input('Teclea el valor: ')) 
                resultado = math.sqrt(val1rc) 
         elif opc_operacion == 7  or opc_operacion == 8  or opc_operacion 
== 9: 
                valgrados = int (input('Teclea los grados: ')) 
                resultado = 
func_operaciones_trigonometricas(opc_operacion, valgrados)             
         else: 
                val1 = float (input('Teclea el primer valor: ')) 
                val2 = float (input('Teclea el segundo valor: ')) 
         if opc_operacion == 1: 
          resultado = func_suma(val1, val2) 
         elif opc_operacion == 2:  
          resultado = func_resta(val1, val2) 
         elif opc_operacion == 3: 
          resultado = func_multiplicacion(val1, val2) 
         elif opc_operacion == 4: 
          resultado = func_division(val1, val2) 
         elif opc_operacion == 6: 
          resultado = func_exponente(val1, val2) 
         return resultado 
 
        #Operación Suma 
        def func_suma(val1, val2): 
          return val1 + val2 
 
        #Operación Resta 
        def func_resta(val1, val2): 
          return val1 - val2 
 
        #Operación Multiplicación 
        def func_multiplicacion(val1, val2): 
          return val1 * val2 
 
         #Operación División 
        def func_division(val1, val2): 
          return val1 / val2 
 
        #Operación Exponente 
        def func_exponente(val1, val2): 
          return val1 ** val2 
 
        #Seno, Coseno, Tangente 
        def func_operaciones_trigonometricas( opc_operacion,  val_grados): 
                    if opc_operacion == 7: 
                     resultado = math.sin(val_grados) 
                    elif opc_operacion == 8: 
                     resultado = math.cos(val_grados) 
                    elif opc_operacion == 9: 
                     resultado = math.tan(val_grados) 
                    return resultado  
 
        def opc_operacion_invalida(): 
            print("Opción inválida, intenta de nuevo") 
            return  
         
        if opc_operacion == 10:       
             break 
        elif opc_operacion > 10: 
             opc_operacion_invalida() 
        else: 
            resultado = func_operacion(opc_operacion) 
         #Asigna el resultado 
            print("El resultado es: " + str(resultado)) 
        resultado = 0 
     
    except ValueError: 
        print("Captura un valor numérico, intenta de nuevo")


￼






