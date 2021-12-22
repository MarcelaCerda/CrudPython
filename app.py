from flask import Flask ,jsonify  #importo el modulo Flask del archivo flask

from productos import productos


app=Flask(__name__)  # inicio Flask y creo un objeto 'app' de Flask
         # le paso como parametro la propiedad __name__     
         # app es mi aplicacion de servidor, va a er mi servidor

@app.route('/ping')
def ping():
    return 'pong'
 
@app.route('/productos')
def getproductos():
    return jsonify(productos)   #tengo que importar jsonify

@app.route('/productos/<string:product_name>')
def getproducto( product_name):
    productoEncontrado=[ producto for producto in productos if producto["name"]==product_name]
    if len(productoEncontrado)>0: 
        return jsonify(productoEncontrado[0])
    else:
        return "no encontrado"







if __name__=='__main__':   # si el nombre del archivo es esta ejecutando como archivo principal 
    app.run(debug=True, port=5000)  
    # inicio  el servidor app como parametro debug, para que si hay cambios 
    # en el fuente se reinicie la aplicacion
    #y le paso el puerto donde se va a ejecutar nuestro servidor ( pueden utilizar otro puerto)

# luego limpiar la consola
# y ejecutar en la terminal  python app.py 
#probar en el navegador      localhost:5000
# va a dar error de server 'Not Found' pero esta bien porque 
# no creamos ninguna ruta