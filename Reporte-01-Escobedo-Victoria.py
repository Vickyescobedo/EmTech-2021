#Para poder entrar con login se debe hacer una lista con los usuarios que entraran al programa y para tener control deesta ista se deberá contar con una persona adminictradora con el usuario y clave para ingresar o eliminar personas en esta lista


USUARIO = 'administrador'
CONTRASENA = 'hola'

username = input('Ingrese su nombre de usuario:\n > ')

if username==USUARIO:
    password = input('Ingrese la contraseña:\n > ')

    if password == CONTRASENA:

        print("Buen día! Bienvenido al programa, Jimmy")
        from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
        #ventas validas

        ventas=[ ] #lista de ventas sin devoluciones
        for sale in lifestore_sales:
            #refund=sale[-1]-- el último de la lista
            refund=sale[4]
            #el uno es tipo entero
            #puede se tipo string
            if refund== 1:
                continue
            #break : para el ciclo totalmente
            #pass: para brincarte ciclo que no quieres hacerlo
            #continue: pasa al siguiente elemento
            else:
                ventas.append(sale)  
        #print(ventas)
        lista_ids=[ ]
        for venta in ventas: #por cada venta en la lista de ventas 
            id_producto=venta[1]
            lista_ids.append(id_producto)


        lista_contadora=[ ]
        id_prod=1
        contador_id=0
        while id_prod<=96:
            for id in lista_ids:
                if id==id_prod:
                    contador_id+=1
            lista_contadora.append(contador_id)
            id_prod+=1
            contador_id=0

        lista_contadora_copia=list(lista_contadora)
        lista_ventas= [ ]
        for venta in lista_contadora:
            if venta!=0:
                lista_ventas.append(venta)

        lista_ventas.sort(reverse=True)

        print('\nDe los productos vendidos los 5 más vendidos anualmente fueron: ')
        x=1
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= lista_contadora_copia.index(lista_ventas[n])
            producto=lifestore_products_copia[posicion]
            categoria=lifestore_products_copia[posicion][3]
            print(x, '.- ', categoria, '| ', producto[1][:20], 'se vendió', lista_ventas[n], 'veces.')
            lista_contadora_copia.pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
            x+=1

        print('\nDe los productos vendidos los 5 menos vendidos anualmente fueron: ')

        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)#se hace una copia de la lista para poder eleiminar la posición y obtener el producto
        lista_contadora_copia=list(lista_contadora)
        while n>=-5:
            posicion= lista_contadora_copia.index(lista_ventas[n])
            producto=lifestore_products_copia[posicion]
            categoria=lifestore_products_copia[posicion][3]
            print(x, '.- ', categoria, '| ', producto[1][:20], 'se vendió', lista_ventas[n], 'veces.')
            lista_contadora_copia.pop(posicion)#donde se elimina el elemento
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1

        #Productos rezagados

        print ('\n Productos rezagados')

        prod_stock=[ ]
        for prod in lifestore_products:
            id_producto=prod[0]
            stock=prod[4]
            categoria=prod[3]
            prod=prod[1][:30]
            sublista=[stock]
            posicion=id_producto-1
            sublista.append(id_producto)
            sublista.append(prod)
            sublista.append(categoria)
            prod_stock.append(sublista)

        n=1
        prod_stock.sort(reverse=True)

        for prod in prod_stock[:10]:
            print(n, prod[3], '|', prod[2], 'en stock: ',prod[0])
            n+=1
        #PARA 5 PRODUCTOS CON MAYOR VENTA
        meses=['/01/','/02','/03/', '/04/','/05/','/06/', '/07/','/08/','/09/','/10/','/11/','/12/']
        ventas_por_mes=[ ] #se crea esta lista con listas vacias para llenarla con los id que se vendieron cada mes
        #donde el indicie 0 va a ser el indice de las ventas en enero, el 1 de febrero y así.
        for mes in meses:
            lista_vacia=[ ]
            ventas_por_mes.append(lista_vacia)

        for venta in ventas: #por cada venta en la lista de ventas 
            id_venta=venta[0] #el id de vneta es posiscion 0 en lista ventas
            fecha=venta[3] #la fecha es la posicion 3 en lista ventas
            id_producto=venta[1] #id del producto es la posicion 1 en lista ventas
            #clasificar en el mes
            #comienzo en el mes 0('/01/')
            contador_de_mes=0
            for mes in meses: #para cada mes en la lista meses
                if mes in fecha: #si el mes está en fecha de la venta
                    ventas_por_mes[contador_de_mes].append(id_producto) #se va agregar a la lista del mes 0 el id del producto de esa venta
                    continue
                contador_de_mes+=1 # una vez que termine con el mes 0 que empiece con el siguient que sepia el contador del mes más 1 es decir 1 y así hasta completar los 12 meses (11 posiciones)
        #print(ventas_por_mes) #ventas_por_mes es una lista que tiene dentro listas de cada id que se vendio en cada mes
        #[[enreo],[febrero].[etc..]]
            #En cada mes esta la lista de los id que se vendieron.

        #para sacar la veces que cada producto se vendió en el mes
        ventas_producto_mensuales= [ ] #en esta lista tendras listas de cada mes
        separacion_meses=[ ] #esta lista representa cada mes y tendrán las veces que se vendió cada id
        contador_id=0  #este contador es para saber cuantas veces se repite el id en un mes
        id=1 #id empieza siendo igual a 1 porque el primer id en lifestore_products es 1
        numero_mes=0 #va a representar el mes y empieza en 0 siendo ENERO
        while numero_mes<=11: #entramos en un bucle while en el que mientras el numero del mes es 0(ENERO) o menor que 11(DICIEMBRE)
            while id<=96: #mientras el id sea igual o menor a 96
                for posicion in ventas_por_mes[numero_mes]: #para cada posicion en en el mes 0 de la lista d eventas mensuales
                    if posicion == id: #si el id en cada posicion es igual a id, y el id comienza siendo 1
                        contador_id+=1 #sumamos 1 al contador de id
                separacion_meses.append(contador_id)  #y el contador lo agregamos a la lista separacion_meses.      
                id+=1 #sumamos 1 a la varible id cada ciclo para que haga lo mismo con los demás id
                contador_id=0 #el contador lo vaciamos cada cilco para que empiece desde 0 al contar cada id
            numero_mes+=1 #sumamos 1 a numero de mes cada ciclo para que haga los mismo cada mes
            id=1 #volvemos a poner el id igual a 1 para que sa
            ventas_producto_mensuales.append(separacion_meses) #agregas la lista separacion_mes a la lista de venta_productos_mensuales
            separacion_meses=[ ]#vaciamos la lista de separacion de meses para que cada mes empiece vacía
        #print(ventas_producto_mensuales) #es una lista que tiene dentro 12 listas que representan cada mes y en cada una de ellas la cantidad de veces que se repite el id de los productos.


        #Ventas ENERO, esto se hace con todos los meses
        print('\nVentas ENERO')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[0]) #hacemos copia de ventas_productos_mensulaes el mes de enero
        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Enero se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= ventas_producto_mensuales[0].index(productos_vendidos_ordenados[n])#obtenemos el indice para saber el id del producto
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[0].pop(posicion)#se elimina el indice para que si se repite el numero lo aparezca el mismo producto
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')#se hace lo mismo que con los más vendidos
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= venta_productos_mensuales_copia.index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[0].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1

        #Ventas FEBRERO
        print('\nVentas FEBRERO')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[1]) #hacemos copia de ventas_productos_mensulaes el mes de enero
        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Febrero se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= ventas_producto_mensuales[1].index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[1].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= venta_productos_mensuales_copia.index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[1].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1


        #Ventas MARZO
        print('\nVentas MARZO')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[2]) #hacemos copia de ventas_productos_mensulaes el mes de enero
        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Marzo se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= ventas_producto_mensuales[2].index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[2].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= venta_productos_mensuales_copia.index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[2].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1


        #Ventas ABRIL
        print('\nVentas ABRIL')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[3]) #hacemos copia de ventas_productos_mensulaes el mes de enero
        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Abril se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= ventas_producto_mensuales[3].index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[3].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= venta_productos_mensuales_copia.index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[3].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1


        #Ventas MAYO
        print('\nVentas MAYOO')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[4]) #hacemos copia de ventas_productos_mensulaes el mes de enero
        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Mayo se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= ventas_producto_mensuales[4].index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[4].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= venta_productos_mensuales_copia.index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[4].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1

        #Ventas Junio
        print('\nVentas JUNIO')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[5]) #hacemos copia de ventas_productos_mensulaes el mes de enero
        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Junio se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= ventas_producto_mensuales[5].index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[5].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= venta_productos_mensuales_copia.index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[5].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
        #Ventas Julio
        print('\nVentas JULIO')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[6]) #hacemos copia de ventas_productos_mensulaes el mes de enero
        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn JuLio se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= ventas_producto_mensuales[6].index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[6].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= venta_productos_mensuales_copia.index(productos_vendidos_ordenados[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', productos_vendidos_ordenados[n], 'veces.')
            ventas_producto_mensuales[6].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
        #AGOSTO

        print('\nVentas AGOSTO')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[7]) #hacemos copia de ventas_productos_mensulaes el mes de enero

        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Agosto se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= ventas_producto_mensuales[7].index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[7].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= venta_productos_mensuales_copia.index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[2].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1
        #SEPTIEMBRE
        print('\nVentas SEPTIEMBRE')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[8]) #hacemos copia de ventas_productos_mensulaes el mes de enero

        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Septiembre se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= ventas_producto_mensuales[8].index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[8].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= venta_productos_mensuales_copia.index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[8].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1

        #octubre
        print('\nVentas octubre')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[9]) #hacemos copia de ventas_productos_mensulaes el mes de enero

        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Octubre se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= ventas_producto_mensuales[9].index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[9].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= venta_productos_mensuales_copia.index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[9].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1

        #Noviembre
        print('\nVentas NOVIEMBRE')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[10]) #hacemos copia de ventas_productos_mensulaes el mes de enero

        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Noviembre se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= ventas_producto_mensuales[10].index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[10].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= venta_productos_mensuales_copia.index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[10].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1

        #DICIEMBRE
        print('\nVentas DICIEMBRE')
        venta_productos_mensuales_copia=list(ventas_producto_mensuales[11]) #hacemos copia de ventas_productos_mensulaes el mes de enero

        ventas_mayores=sorted(venta_productos_mensuales_copia,reverse=True) #ordenamos la lista de mayor a menor
        productos_vendidos=[ ] #creamos una lista donde se vendieron 1 o más productos

        for venta in venta_productos_mensuales_copia: #hacemos un bucle para detectar las ventas diferentes a 0 y no tomarlas en cuenta
            if venta!=0:
                productos_vendidos.append(venta)#se agrega todo producto que se haya vendido 1 o más veces
        productos_vendidos_ordenados=sorted(productos_vendidos)#se ordenan de menor a mayor para sacar los menos vendidos 
        cantidad_de_ventas=sum(productos_vendidos)#se suman las ventas de cada producto para obtener las ventas totales del mes

        print('\nEn Diciembre se vendieron:', len(productos_vendidos),'productos diferentes''. ''Que suman un total de:', cantidad_de_ventas,'ventas')
        print('\nDe los productos vendidos los 5 más vendidos fueron:')
        x=1
        n=0
        lifestore_products_copia=list(lifestore_products)
        while n<=4:
            posicion= ventas_producto_mensuales[11].index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(x, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[11].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n+=1
            x+=1
        print('\nDe los productos vendidos los 5 menos vendidos fueron: ')
        venta_productos_mensuales_copia=list(venta_productos_mensuales_copia)
        n=-1
        lifestore_products_copia=list(lifestore_products)
        while n>=-5:
            posicion= venta_productos_mensuales_copia.index(ventas_mayores[n])
            producto=lifestore_products_copia[posicion]
            print(n+1, '.- ', producto[3],'|', producto[1][:20], 'se vendió', ventas_mayores[n], 'veces.')
            ventas_producto_mensuales[11].pop(posicion)
            lifestore_products_copia.pop(posicion)
            n-=1

        #10 PRODUCTOS CON MAYORES BÚSQUEDAS
        contador_busqueda=0
        busquedas=[ ]
        id_producto=1

    #se hace un bucle buscando todos los productos que hayan sido buscados agregandolos a una lista nueva
        while id_producto<=96:
            for busqueda in lifestore_searches: 
                posicion=busqueda[1]
                if posicion== id_producto:
                    contador_busqueda+=1    
            busquedas.append(contador_busqueda)
            id_producto+=1
            contador_busqueda=0
        #print (busquedas)    

        productos_buscados=[ ]   
        for busqueda in busquedas: #hacemos un bucle para detectar las busquedas diferentes a 0 y no tomarlas en cuenta
            if busqueda!=0:
                productos_buscados.append(busqueda)#se agrega todo producto que se haya buscado al menos 1 vez
        productos_buscados_ordenados=sorted(productos_buscados)#se ordenan de menor a mayor para sacar los menos buscados 
        cantidad_de_busquedas=sum(productos_buscados)#se suman las busquedas de cada producto para obtener las busquedas totales 
        busquedas_totales=sum(productos_buscados)

        print('\nSe realizaron ', busquedas_totales, 'busquedas de ', len(productos_buscados), 'productos buscados')

        busquedas_copia=list(busquedas)
        busquedas_copia_ordenada=sorted(busquedas_copia, reverse=True)
        mayores_busquedas=busquedas_copia_ordenada[0:10]

        print('\nDe los productos buscados los 10  más buscados son: ')

        n=0
        lifestore_products_copia=list(lifestore_products)

        while n<=9:
            posicion1=busquedas_copia.index(mayores_busquedas[n])
            producto=lifestore_products_copia[posicion1]
            categoria= lifestore_products_copia[posicion1][3]
            print(n+1,'.- ', categoria, '| ', producto[1][:30], '| ','se buscó', mayores_busquedas[n], 'veces')
            busquedas_copia.pop(posicion1)
            lifestore_products_copia.pop(posicion1)
            n+=1
        #10 productos con menos busquedas
        print('\nDe los productos buscados los 10 menos buscados son: ')

        n=0
        lifestore_products_copia=list(lifestore_products)
        busquedas_copia=list(busquedas)

        while n<=9:
            posicion1=busquedas_copia.index(productos_buscados_ordenados[n])
            producto=lifestore_products_copia[posicion1]
            categoria= lifestore_products_copia[posicion1][3]
            print(n+1,'.- ', categoria, '| ', producto[1][:30], '| ','se buscó', productos_buscados_ordenados[n], 'veces')
            busquedas_copia.pop(posicion1)
            lifestore_products_copia.pop(posicion1)
            n+=1

        # #dividir lifestore_sales en meses
        # meses=['/01/','/02','/03/', '/04/','/05/','/06/', '/07/','/08/','/09/','/10/','/11/','/12/']
        # ventas_por_mes=[ ] #se crea esta lista con listas vacias para llenarla con los id que se vendieron cada mes
        # #donde el indicie 0 va a ser el indice de las ventas en enero, el 1 de febrero y así.
        # for mes in meses:
        #     lista_vacia=[ ]
        #     ventas_por_mes.append(lista_vacia)
        # for venta in lifestore_sales: #por cada venta en la lista de ventas 
        #     id_venta=venta[0] #el id de vneta es posiscion 0 en lista ventas
        #     fecha=venta[3] #la fecha es la posicion 3 en lista ventas
        #     id_producto=venta[1] #id del producto es la posicion 1 en lista ventas
        #     #clasificar en el mes
        #     #comienzo en el mes 0('/01/')
        #     contador_de_mes=0
        #     for mes in meses: #para cada mes en la lista meses
        #         if mes in fecha: #si el mes está en fecha de la venta
        #             ventas_por_mes[contador_de_mes].append(id_producto) #se va agregar a la lista del mes 0 el id del producto de esa venta
        #             continue
        #         contador_de_mes+=1
        # print(ventas_por_mes)


        # ventas_producto_mensuales=[0,0,0,0,0,0,0,0,0,0,0,0]

        # ventas_meses=[ ]
        # for producto in lifestore_products:
        #     prod_rev_cant=[0,0,0]
        #     ventas_meses.append(prod_rev_cant)

        # n=0
        # for mes in meses:
        #     ventas_producto_mensuales[n]=(ventas_meses)
        #     n+=1
        # #print(ventas_producto_mensuales)


        # print(prod_rev_cant)
        # contador_id=0  #este contador es para saber cuantas veces se repite el id en un mes
        # id=1 #id empieza siendo igual a 1 porque el primer id en lifestore_products es 1
        # numero_mes=0 #va a representar el mes y empieza en 0 siendo ENERO
        # while numero_mes<=0: #entramos en un bucle while en el que mientras el numero del mes es 0(ENERO) o menor que 11(DICIEMBRE)
        #     while id<=1: #mientras el id sea igual o menor a 96
        #         for posicion in ventas_por_mes[numero_mes]: #para cada posicion en en el mes 0 de la lista d eventas mensuales
        #             if posicion == id: #si el id en cada posicion es igual a id, y el id comienza siendo 1
        #                 contador_id+=1 #sumamos 1 al contador de id
        #                 print(contador_id)
        #         prod_rev_cant[2]=contador_id  #y el contador lo agregamos a la lista separacion_meses.
        #         prod_rev_cant[1]=id 
        #         prod_rev_cant[0]=0
        #         print(prod_rev_cant)
        #         ventas_producto_mensuales[numero_mes][id]=prod_rev_cant
        #         print(ventas_producto_mensuales)
        #         id+=1 #sumamos 1 a la varible id cada ciclo para que haga lo mismo con los demás id
        #         contador_id=0 #el contador lo vaciamos cada cilco para que empiece desde 0 al contar cada id
        #     numero_mes+=1 #sumamos 1 a numero de mes cada ciclo para que haga los mismo cada mes
        #     id=1 #volvemos a poner el id igual a 1 para que sa
        #     prod_rev_cant=[0,0,0]
        # print(ventas_producto_mensuales)


        #dividir lifestore_sales en meses
        meses=['/01/','/02','/03/', '/04/','/05/','/06/', '/07/','/08/','/09/','/10/','/11/','/12/']
        ventas_por_mes=[ ] #se crea esta lista con listas vacias para llenarla con los id que se vendieron cada mes
        #donde el indicie 0 va a ser el indice de las ventas en enero, el 1 de febrero y así.
        for mes in meses:
            lista_vacia=[ ]
            ventas_por_mes.append(lista_vacia)
        for venta in lifestore_sales: #por cada venta en la lista de ventas 
            id_venta=venta[0] #el id de vneta es posiscion 0 en lista ventas
            fecha=venta[3] #la fecha es la posicion 3 en lista ventas
            id_producto=venta[1] #id del producto es la posicion 1 en lista ventas
            #clasificar en el mes
            #comienzo en el mes 0('/01/')
            contador_de_mes=0
            for mes in meses: #para cada mes en la lista meses
                if mes in fecha: #si el mes está en fecha de la venta
                    ventas_por_mes[contador_de_mes].append(id_producto) #se va agregar a la lista del mes 0 el id del producto de esa venta
                    continue
                contador_de_mes+=1
        # print(ventas_por_mes)

        #reseñas
        print('\nReseñas')

        prod_reviews=[ ]
        for prod in lifestore_products:
            id_producto=prod[0]
            sublista=[id_producto,0,0]
            prod_reviews.append(sublista)

        for venta in lifestore_sales:
            id_prod= venta[1]
            review= venta[2]
        
            indice= id_prod - 1
            prod_reviews[indice][1]+=review
            prod_reviews[indice][2]+=1

        for indice, lista in enumerate(prod_reviews):
            suma=lista[1]
            cant=lista[2]
            if cant>0:
                calif_prom= suma/cant
                prod_reviews[indice][1]=calif_prom

        #mejores calificados
        mejores_calificados=[ ]
        for lista in prod_reviews:
            sublista=[lista[1], lista[0]]  
            mejores_calificados.append(sublista)  

        mejores_calificados.sort(reverse=True)
        print('\nLos 5 productos con mejor calificación son:')

        for rev in mejores_calificados[:5]:
            id_prod=rev[1]
            prom_rev=rev[0]
            for producto in lifestore_products:
                if producto[0]==id_prod:
                    print(rev[0], '| ', rev[1],'| ', producto[1][:20])

        print('\n Los 5 productos con menor calificación son:')
        mejores_calificados.sort()


        for rev in mejores_calificados[:5]:
            id_prod=rev[1]
            prom_rev=rev[0]
            for producto in lifestore_products:
                if producto[0]==id_prod:
                    print(rev[0], '| ', rev[1],'| ', producto[1][:20])

        #mejores vendidos
        mejores_vendidos=[ ]
        for lista in prod_reviews:
            sublista=[lista[2], lista[0], lista[1]]  #lista[2]=ventas, lista[0]=id, lista[1]=calificación
            mejores_vendidos.append(sublista)  
        print('\n De los 5 productos más vendidos, las reseñas son: ' )
        mejores_vendidos.sort(reverse=True)
        for rev in mejores_vendidos[:5]:
            id_prod=rev[1]
            prom_rev=rev[2]
            for producto in lifestore_products:
                if producto[0]==id_prod:
                    print(rev[2], '| ', rev[1],'| ', producto[1][:20])


        # for rev in mejores_vendidos[:5]:
        #     print(rev)  
        print('\n De los 5 productos menos vendidos, las reseñas son  ')

        lista_vendidos_reseña=[ ] # se crea una lista para contener sólo los productos que se han vendido y que tienen
        for reseña in mejores_vendidos:
            if reseña[0]!=0:
                lista_vendidos_reseña.append(reseña)
                lista_vendidos_reseña.sort( )

        for rev in lista_vendidos_reseña[:5]:
            id_prod=rev[1]
            prom_rev=rev[2]
            for producto in lifestore_products:
                if producto[0]==id_prod:
                    print(rev[2], '| ', rev[1],'| ', producto[1][:20])

        #GANANCIAS MENSUALES


        gancias_mensuales = []
        for venta_mensual in ventas_por_mes:
            ganancia_del_mes = 0
            for id_venta in venta_mensual:
                indice_de_venta = id_venta - 1
             
                info_de_venta = lifestore_sales[indice_de_venta]

                id_prod = info_de_venta[1]
                indice_de_prod = id_prod - 1
                info_del_prod = lifestore_products[indice_de_prod]
                precio_de_prod = info_del_prod[2]
                ganancia_del_mes = ganancia_del_mes + precio_de_prod
            gancias_mensuales.append(ganancia_del_mes)

        lista_prev = []
        for mes, ganancia in enumerate(gancias_mensuales):
            sublista = [ganancia, mes+1] #mes+1 sería el mes correcto
            lista_prev.append(sublista)

        print('\n Ventas ordenadas por mes: ')

        for lista in lista_prev:
            print(lista)

        lista_prev.sort(reverse=True)

        print('\n Ventas de cada mes, ordenadas de mayor a menor')
        for lista in lista_prev:
            print(lista)

        #total de ingresos
        print('\n Total de ingresos:')
        total_ingresos=sum(gancias_mensuales)
        print ('\n Se obtuvieron un total de : ', total_ingresos, 'ingresos')


        # # cantidad_ventas_mensuales = []
        # # for venta_mensual in ventas_por_mes:
        # #     cantidad_ventas_mensuales=len(venta_mensual)
        # #     print(cantidad_ventas_mensuales)
    else:
        print("Contraseña erronea")
else:
    print('El usuario no existe')
