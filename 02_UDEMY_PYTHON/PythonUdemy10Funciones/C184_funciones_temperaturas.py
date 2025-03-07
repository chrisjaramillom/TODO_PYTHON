print('*** Sistema TRANSFORMACION TEMPARATURA ***')

def tem_cen_far():
    print('--- CENTIGRADOS A FARENHEI ---')
    centigrados = float(input('Ingresa temperatura en  grados centigrados:'))
    farenhei = (centigrados * 1.8) + 32
    print(f'Los {centigrados:.2f} centigrados equivalen a {farenhei:.2f} Farenhei')

def tem_far_cen():
    print('--- FARENHEI A CENTIGRADOS ---')
    farenhei = float(input('Ingresa temperatura en  grados farenhei:'))
    centigrados = (farenhei - 32) * 5 / 9
    print(f'Los {farenhei:.2f} farenhei equivalen a {centigrados:.2f} centigrados')

# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        print(f'''Menú temperaturas:
        1. CENTIGRADOS A FARENHEI
        2. FARENHEI A CENTIGRDOS    
        3. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            tem_cen_far()
        elif opcion == 2:
            tem_far_cen()
        elif opcion == 3:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, proporciona otra opción!')
