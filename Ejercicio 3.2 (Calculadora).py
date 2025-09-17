
operacion = input('Ingrese la operacion que quiere efectuar: ')

a = input('Ingrese el 1er valor: ')

b = input('Ingrese el 2do valor: ')


def sumar (a, b):
    return a+b

def restar (a, b):
    return a-b

def multiplicar (a, b):
    return a*b  

def dividir (a, b):
    return a//b  

def calculadora_simple (operacion, a, b):
    try:
        a=int(a)
        b=int(b)

        if operacion == 'sumar':
            return sumar(a,b)
        elif operacion == 'restar':
            return restar(a,b)
        elif operacion == 'multiplicar':
            return multiplicar(a,b)
        elif operacion == 'dividir':
            return dividir(a,b)
        else:
            return KeyError ('Operacion no valida')
        
    except ZeroDivisionError :
        return 'Error: No se puede dividir por cero'
    
    except ValueError:
        return 'Error: Los valores deben ser numeros'
    

#print (calculadora_simple(f'El resultado de la {operacion} es =  {a}, {b}'))
print (f'El resultado de {operacion} = {(calculadora_simple(operacion, a,b))}')

print ('Simpre para ayudarte')
