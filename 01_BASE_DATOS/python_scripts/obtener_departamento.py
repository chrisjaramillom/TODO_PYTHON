import sys
import json
from departamento_crud import obtener_departamento_por_id

if len(sys.argv) != 2:
    print(json.dumps({"success": False, "message": "ID no proporcionado"}))
    sys.exit(1)

id = int(sys.argv[1])
departamento = obtener_departamento_por_id(id)

if departamento:
    print(json.dumps({"success": True, "data": departamento}))
else:
    print(json.dumps({"success": False, "message": "Departamento no encontrado"}))