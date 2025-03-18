import sys
import json
from departamento_crud import crear_departamento

if len(sys.argv) != 4:
    print(json.dumps({"success": False, "message": "Argumentos insuficientes"}))
    sys.exit(1)

nombre = sys.argv[1]
ubicacion = sys.argv[2]
bandera = int(sys.argv[3])

success = crear_departamento(nombre, ubicacion, bandera)
print(json.dumps({"success": success}))