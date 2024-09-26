

## What is int in python

## [INT:](https://www.geeksforgeeks.org/python-int-function/)

## [Como usar if, elif else en python]()

## [Sentencia if ]()

Si la condición que sigue a la palabra clave if  se evalúa como verdadera, el bloque de código se ejecutará. Ten en cuenta que los paréntesis no se utilizan antes y después de la verificación de condición como en otros idiomas.

    if True:
      print('¡el bloque If se ejecutará!')

## [Sentencia else]()

Opcionalmente, puedes agregar una respuesta else que se ejecutará si la condición es false

    if not True:
      print('¡La sentencia If se ejecutará!')
    else:
      print('¡La sentencia Else se ejecutará!')
    O también puedes ver este ejemplo:

    y = 3

    if y > 4:
      print("¡No voy a imprimir!") #esta sentencia no se ejecuta
    else:
      print("¡La condición no era verdadera!") #esta sentencia se ejecuta


## [Sentencia elif]()

Se pueden verificar varias condiciones al incluir una o más verificaciones elif después de su declaración if inicial. Ten en cuenta que solo se ejecutará una condición:


    z = 7

    if z > 8:
      print("¡No voy a imprimir!") #esta sentencia no se ejecuta
    elif z > 5:
      print("¡Yo lo haré!") #esta sentencia se ejecuta
    elif z > 6:
      print("¡Tampoco voy a imprimir!") #esta sentencia no se ejecuta
    else:
      print("¡Yo tampoco!") #esta sentencia no se ejecuta



Nota: solo se ejecutará la primera condición que se evalúe como true. Aunque z > 6 es true, el bloque if/elif/else termina después de la primera condición verdadera. Esto significa que un else solo se ejecutará si ninguna de las condiciones es true.

## [Sentencias if anidadas]()

También podemos crear if anidados para la toma de decisiones.

Tomemos un ejemplo de cómo encontrar un número que sea par y también mayor que 10

python 

    x = 34
    if x %  2 == 0:  # así es como creas un comentario y ahora comprueba número par.
      if x > 10:
        print("Este número es par y es mayor que 10")
      else:
        print("Este número es par, pero no mayor 10")
    else:
      print ("El número no es par. Así que punto de verificación más.")

Este fue solo un ejemplo simple de if anidados. No dudes en explorar más en línea.

Si bien los ejemplos anteriores son simples, puedes crear condiciones complejas utilizando comparaciones booleanas y operadores booleanos.

Declaración if-else de Python en línea
También podemos usar declaraciones if-else en funciones de Python en línea. El siguiente ejemplo debe verificar si el número es mayor o igual que 50, si es así, retorna True:

python 

    x = 89
    es_mayor = True if x >= 50 else False

    print(es_mayor)
    
    Salida:

    >
    True
    >


