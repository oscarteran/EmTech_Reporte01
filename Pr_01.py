"""
Autor:
        OSCAR HERNANDEZ TERAN

Instrucciones del programa:
    1. Categorias con menores ventas y categorias con menores busquedas
    2. Categorias con mayores ventas y categorias con mayores busquedas
    3. Sugerir una estrategia de productos a retirar del mercado asi 
       como sugerencias de como reducir la acumulacion de inventario 
       considerando los datos mensuales.  



------------------------------------------------------------
-------INFORMACION A CERCA DE LA BASE DE DATOS--------------
------------------------------------------------------------
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]


------------------------------------------------------------
-------------------------NOTA-------------------------------
---- Por buena practica, y para que el codigo pueda ser ----
---- plasmadode manera correcta en LATEX, este programa ----
------------- sera comentado sin acentos--------------------  
------------------------------------------------------------

"""

# Importamos la Base de datos
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#


# -----------------------------------------------------------------------
# -----Primera inspeccion de la estructura de la Base de datos (BD)------
# -----------------------------------------------------------------------
print('-'*100)
print('Estructura de la BD de búsqueda:\n')
for i in range(5):
    print('id_search: ', lifestore_searches[i][0],' | ', 'id_product: ', lifestore_searches[i][1])
 
print('-'*100)
print('Estructura de la BD de ventas:\n')
for i in range(5):
    print('id_sale:  ', lifestore_sales[i][0], ' | ', 'id_product: ', lifestore_sales[i][1], ' | ', 
          'score: ',lifestore_sales[i][2], ' | ', 'date: ', lifestore_sales[i][3], ' | ',
          'refund: ',lifestore_sales[i][4]
         )

print('-'*100)
print('Estructura de la BD de Productos:\n')
for i in range(5):
    print('id_sale:  ', lifestore_products[i][0], '\n', 
          'name:  ', lifestore_products[i][1], '\n',
          'price:  ', lifestore_products[i][2], ' | ', 'category:  ', lifestore_products[i][3], ' | ',
          'stock:  ', lifestore_products[i][4], ' | \n', 
         )


# -----------------------------------------------------------------------
# ----------------------------Login--------------------------------------
# -----------------------------------------------------------------------
def login():
    '''
    '''
    print(' |---------------------------------------------------|\n',
          '|-----------------LOGIN-----------------------------|\n',
          '|---------------------------------------------------|\n')

    user_C = 'Oscar' 
    pass_C = 'asdfgh'
    Intentos = 0
    
    while True:
        print('*'*25)
        print('Ingrese sus credenciales: \n')
        user  = input('Nombre de usuario: ')
        passw = input('Contraseña: ')

        Intentos += 1

        if Intentos == 5:
            print('*'*25)
            print('Permiso denegado.')
            print('Interrumpiendo ejecucion del programa')
            print('*'*25)
            exit()
        if user == user_C and passw == pass_C:
            print()
            print('*'*25)
            print('SUS DATOS SON CORRECTOS.')
            print('*'*25, '\n')
            input('Presione "Enter" para continuar:')
            break
        else:
            print('Intento fallido No. {} \n \n'.format(Intentos))
        
# Llamamos a la funcion
#login()


# -----------------------------------------------------------------------
# ------------------- Productos mas vendidos ----------------------------
# -----------------------------------------------------------------------

# Listamos los 50 productos mas vendidos
id_s = []
ventas_total = []

for ventas in lifestore_sales:
    id_s.append(ventas[1])

for idx, produc in enumerate(lifestore_products):
    ventas_total.append({
        'id':produc[0],
        'name':produc[1], 
        'total':id_s.count(idx+1)
    })

# Ordenamos a partir de una llave
ventas_total = sorted(ventas_total, key=lambda x:x['total'], reverse=True)

# 50 articulos mas vendidos
top_50 = ventas_total[:50]


# Impresion de los primeros 5 productos
print('-------------------------------------------------')
print('-----------Productos mas vendidos----------------')
print('-------------------------------------------------')
for i in range(5):
    print(
        ' Ventas  : ', top_50[i]['total'], '\n',
        'Producto: ', top_50[i]['name'], '\n', 
    )


# -----------------------------------------------------------------------
# ------------------- Productos mas buscados ----------------------------
# -----------------------------------------------------------------------
_ids = []
busquedas_t = []

for busq in lifestore_searches:
    _ids.append(busq[1])

for produc in lifestore_products:
    busquedas_t.append(
        {'id':produc[0],
         'Name':produc[1],
         'Busquedas':_ids.count(produc[0])
         }
    )

busquedas_total = sorted(busquedas_t, key=lambda x:x['Busquedas'], reverse=True)

# Impresion de los primeros 5 productos
print('-------------------------------------------------')
print('-----------Productos mas buscados----------------')
print('-------------------------------------------------')
for i in range(5):
    print(
        ' Busquedas: ', busquedas_total[i]['Busquedas'], '\n',
        'Producto: ', busquedas_total[i]['Name'], '\n', 
    )



# -----------------------------------------------------------------------
# --------------- 50 menores ventas por categoria -----------------------
# -----------------------------------------------------------------------
categorias = [catego[3] for catego in lifestore_products]
unique_categorias = list(dict.fromkeys(categorias))


categorias = {
     'procesadores'     :[],
    'tarjetas de video':[], 
    'tarjetas madre'   :[], 
    'discos duros'     :[], 
    'memorias usb'     :[], 
    'pantallas'        :[], 
    'bocinas'          :[], 
    'audifonos'        :[]   
}

# Invertimos el orden de venta
ventas_total_50 = ventas_total[:50]
ventas_total_i = ventas_total_50[::-1]

# Organizamos por categoria
for ventas in ventas_total_i:
    for productos in lifestore_products:
        if ventas['name'] == productos[1]:
            categorias[productos[3]].append([ventas['name'], ventas['total']])


# Impresion de los primeros 5 productos por categoria
print('-------------------------------------------------')
print('---------Productos con menos ventas--------------')
print('-------------------------------------------------')
for name in categorias:
    print('CATEGORIA: ', name)
    for i in range(len(categorias[name])):
        if i > 5:
            break
        else:
            print(' Nombre: ', categorias[name][i][0], '\n',
                  'Ventas:  ', categorias[name][i][1] )
    print()        

# -----------------------------------------------------------------------
# ------------- 100 con menores busquedas por categoria------------------
# -----------------------------------------------------------------------
categorias_busqueda = {
     'procesadores'     :[],
    'tarjetas de video':[], 
    'tarjetas madre'   :[], 
    'discos duros'     :[], 
    'memorias usb'     :[], 
    'pantallas'        :[], 
    'bocinas'          :[], 
    'audifonos'        :[]   
}


# Invertimos la lista de busqueda
busquedas_total_i = busquedas_total[::-1]

# Organizamos por categoria
for busqueda in busquedas_total_i:
    for productos in lifestore_products:
        if busqueda['Name'] == productos[1]:
            categorias_busqueda[productos[3]].append(
                [busqueda['Name'], 
                busqueda['Busquedas']])


# Impresion de los primeros 5 productos por categoria
print('-------------------------------------------------')
print('--------Productos con menos busquedas------------')
print('-------------------------------------------------')
for name in categorias_busqueda:
    print('CATEGORIA: ', name)
    for i in range(len(categorias_busqueda[name])):
        if i > 5:
            break
        else:
            print(' Nombre:   ', categorias_busqueda[name][i][0], '\n',
                  'Busquedas: ', categorias_busqueda[name][i][1] )
    print() 


# -----------------------------------------------------------------------
# ------------Productos por reseña en el servicio------------------------
# -----------------------------------------------------------------------
# Creamos las listas para almacenar
# cali_completa = []
# top_20_cali = []
# botton_20_cali = []

# calificaciones = sorted(lifestore_sales, key=lambda x:x[2], reverse=True)
# calificaciones_i = calificaciones[::-1]

# id_en_ventas = lifestore_sales[1]

# for venta in lifestore_sales:
#     for producto in lifestore_products:
#         if venta[1] == producto[0]:
#             cali_completa.append([
#                 venta[1],producto[1], venta[2], 
#             ])

cali_total = []
for id in lifestore_sales:
    cali_total.append(id[1])

cali_unicas = list(dict.fromkeys(cali_total))
cali_unicas_r = []
for i in range(len(cali_unicas)):
    cali_unicas_r.append([cali_unicas[i], cali_total.count(cali_unicas[i])])

cali_unicas_nombre = []
for id in cali_unicas:
    for producto in lifestore_products:
            if id == producto[0]:
                cali_unicas_nombre.append(producto[1])

print(cali_unicas_r)


# -----------------------------------------------------------------------
# ----------Ingresos y ventas en ventanas de tiempo----------------------
# -----------------------------------------------------------------------



















