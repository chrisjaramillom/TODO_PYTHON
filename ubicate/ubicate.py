import folium
from geopy.geocoders import Nominatim

# Inicializar el geocodificador
geolocator = Nominatim(user_agent="geo_locator")

# Crear un mapa base
mapa = folium.Map(location=[0, 0], zoom_start=2)

def buscar_ubicacion():
    """Buscar una ubicación por nombre o dirección"""
    ubicacion = input("Ingrese una ubicación para buscar en el mapa: ")
    try:
        localizacion = geolocator.geocode(ubicacion)
        if localizacion:
            print(f"Ubicación encontrada: {localizacion.address}")
            print(f"Coordenadas: {localizacion.latitude}, {localizacion.longitude}")
            folium.Marker(
                [localizacion.latitude, localizacion.longitude],
                popup=localizacion.address,
                icon=folium.Icon(color="blue")
            ).add_to(mapa)
        else:
            print("Ubicación no encontrada. Intenta con otra dirección.")
    except Exception as e:
        print(f"Error al buscar ubicación: {e}")

def agregar_coordenadas():
    """Agregar una ubicación con coordenadas manuales"""
    try:
        latitud = float(input("Ingrese la latitud: "))
        longitud = float(input("Ingrese la longitud: "))
        lugar = geolocator.reverse((latitud, longitud), language='en')
        direccion = lugar.address if lugar else "Lugar desconocido"
        print(f"Lugar encontrado: {direccion}")
        folium.Marker(
            [latitud, longitud],
            popup=direccion,
            icon=folium.Icon(color="green")
        ).add_to(mapa)
    except Exception as e:
        print(f"Error al agregar coordenadas: {e}")

def guardar_mapa():
    """Guardar el mapa interactivo en un archivo HTML"""
    nombre_archivo = input("Ingrese el nombre del archivo para guardar el mapa (sin extensión): ")
    mapa.save(f"{nombre_archivo}.html")
    print(f"Mapa guardado como {nombre_archivo}.html")

# Menú principal
def menu():
    salir = False
    while not salir:
        print("\n*** Menú de Funcionalidades ***")
        print("1. Buscar una ubicación")
        print("2. Agregar coordenadas manuales")
        print("3. Guardar el mapa en un archivo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            buscar_ubicacion()
        elif opcion == "2":
            agregar_coordenadas()
        elif opcion == "3":
            guardar_mapa()
        elif opcion == "4":
            salir = True
            print("¡Gracias por usar el sistema!")
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
menu()
