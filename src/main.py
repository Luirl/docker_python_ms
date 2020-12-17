'''
FICHERO PRINCIPAL DEL MICROSERVICIO
Este fichero contiene:
- el código básico del microservicio
- la definición de los endpoints que se ofrecerán al exterior
- las clases que implementan esos endpoints.
'''

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from werkzeug.exceptions import BadRequest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from common.math_operations import multiply, divide

'''
Inicialización básica
'''
app = Flask(__name__)
api = Api(app)


'''
Implementación del primer microservicio. Cada método que define corresponde a un método
HTTP equivalente. Si no está implementado, no se ofrece a través del API.
'''
class MultiplyBy(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument('number', required=True,
            help='No number to multiply provided: {error_msg}', location='json')
        super(MultiplyBy, self).__init__()

    def get(self):
        pass

    def post(self, factor):
        try:
            args = self.reqparse.parse_args()
            try:
                number = int(args.number)
            except ValueError:
                return {'error': "variable 'number' must be an int"}, 400

            return {'number': number, 'factor': factor, 'result': multiply(number, factor)}, 200
        except BadRequest:
            abort(400)
        except Exception as e:
            return {"error": e.message}, 500


'''
Implementación del segundo microservicio. Se pueden implementar tantos como sea necesario.
'''
class DivideBy(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument('number', required=True,
                                   help='No number to divide provided: {error_msg}', location='json')
        super(DivideBy, self).__init__()

    def get(self):
        pass

    def post(self, divisor):
        try:
            args = self.reqparse.parse_args()
            try:
                number = int(args.number)
            except ValueError:
                return {'error': "variable 'number' must be an int"}, 400

            if divisor == 0:
                return {'error': "Division by zero not allowed"}, 400

            return {'number': number, 'divisor': divisor, 'result': divide(number, divisor)}, 200
        except BadRequest:
            abort(400)
        except Exception as e:
            return {"error": e.message}, 500
            # abort(500, e.message)


'''
Asociación de los microservicios implementados a rutas HTTP. Las rutas pueden contener parámetros (como el factor o 
el divisor).  
'''
api.add_resource(MultiplyBy, '/v1.0/MultiplyBy/<int:factor>')
api.add_resource(DivideBy, '/v1.0/DivideBy/<int:divisor>')


'''
Si se ejecuta directamente el main.py, sucede que __name__ == "__main__" y entonces se arranca un pequeño servidor
para pruebas.  
'''
if __name__ == "__main__":
    app.run(debug=True)