import sys
import json
from departamento_crud import actualizar_departamento

if len(sys.argv) != 5:
    print(json.dumps({"success": False, "message": "Argumentos insuficientes"}))
    sys.exit(1)

id = int(sys.argv[1])
nombre = sys.argv[2]
ubicacion = sys.argv[3]
bandera = int(sys.argv[4])

success = actualizar_departamento(id, nombre, ubicacion, bandera)
print(json.dumps({"success": success}))