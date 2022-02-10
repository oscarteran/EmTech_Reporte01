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
-- Por costumbre, y para que el codigo pueda ser plasmado --
----- de manera correcta en LATEX, este programa sera ------
--------------- comentado sin acentos ----------------------  
------------------------------------------------------------

"""

# Importamos las librerias
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches



# Primera inspeccion de la Base de datos (BD)
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





