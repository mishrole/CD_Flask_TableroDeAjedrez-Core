from flask import Flask, render_template

app = Flask(__name__)

def generarTablero(filas = 8, columnas = 8, primario = 'red', secundario = 'black'):
    tablero = []

    # Determina la generación del tablero empezando por las filas
    for f in range(0, filas):
        fila = []
        
        # Por defecto inicia con el color primario y finaliza con el secundario
        inicio = primario
        final = secundario
        
        # Si el índice de la fila es impar, cambia el orden de colores
        if f % 2 != 0:
            # Ahora inicia con el color secundario
            inicio = secundario
            # Y finaliza con el color primario
            final = primario

        # Determina la generación de columnas de la fila actual
        for c in range(0, columnas):

            # Si el índice de la columna es par, la columna es del color inicial
            if c % 2 == 0:
                fila.append(inicio)
            # Caso contrario, la columna es del color final
            else:
                fila.append(final)

        # Al finalizar el cálculo de columnas en la fila actual, se añade al tablero
        tablero.append(fila)
    
    # Retorna el tablero completo como arreglo bidimensional de colores
    return tablero

@app.errorhandler(404)
def not_found(e):
    return "<p>¡Lo siento! No hay respuesta. Inténtalo otra vez</p>"

@app.route('/', methods=['GET'])
def index():
    return render_template("chess.html", tablero = generarTablero())

@app.route('/<int:limiteFilas>', methods=['GET'])
def limitarFilas(limiteFilas):
    return render_template("chess.html", tablero=generarTablero(filas = limiteFilas))

@app.route('/<int:limiteFilas>/<int:limiteColumnas>', methods=['GET'])
def limitarFilasYColumnas(limiteFilas, limiteColumnas):
    return render_template("chess.html", tablero = generarTablero(filas = limiteFilas, columnas = limiteColumnas))

@app.route('/<int:limiteFilas>/<int:limiteColumnas>/<cambiarPrimario>', methods=['GET'])
def limitarFilasYColumnasYPrimario(limiteFilas, limiteColumnas, cambiarPrimario):
    return render_template("chess.html", tablero = generarTablero(filas = limiteFilas, columnas = limiteColumnas, primario = cambiarPrimario))

@app.route('/<int:limiteFilas>/<int:limiteColumnas>/<cambiarPrimario>/<cambiarSecundario>', methods=['GET'])
def limitarFilasYColumnasYPrimarioYSecundario(limiteFilas, limiteColumnas, cambiarPrimario, cambiarSecundario):
    return render_template("chess.html", tablero = generarTablero(filas = limiteFilas, columnas = limiteColumnas, primario = cambiarPrimario, secundario = cambiarSecundario))

if __name__ == "__main__":
    app.run( debug = True )