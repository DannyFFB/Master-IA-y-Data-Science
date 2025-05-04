"""5- Una función donde se definan 8 variables de diferente tipo y 
me imprima que tipo de datos son"""

def tipos_de_datos():
    
    entero = 10                
    decimal = 3.14              
    texto = "Hola mundo"        
    booleano = True             
    lista = [1, 2, 3]           
    tupla = (4, 5, 6)           
    diccionario = {"a": 1, "b": 2}  
    conjunto = {7, 8, 9}        

   
    print(type(entero))
    print(type(decimal))
    print(type(texto))
    print(type(booleano))
    print(type(lista))
    print(type(tupla))
    print(type(diccionario))
    print(type(conjunto))

tipos_de_datos()