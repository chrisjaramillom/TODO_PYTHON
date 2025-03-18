import sys
import json
from departamento_crud import eliminar_departamento

if len(sys.argv) != 2:
    print(json.dumps({"success": False, "message": "ID no proporcionado"}))
    sys.exit(1)

id = int(sys.argv[1])
success = eliminar_departamento(id)
print(json.dumps({"success": success}))