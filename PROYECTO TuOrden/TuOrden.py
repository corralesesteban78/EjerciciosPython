#---------------------TuOrden-------------------------#
import win32print

producto = ""
salsa = ""
toppings = []
helado = ""
michelar = ""
base = ""


#---------Tamaño de vasos------------#
def tamano_vasos():

    print("""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║ ████████╗ █████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗    ║
║ ╚══██╔══╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║██╔═══██╗   ║
║    ██║   ███████║██╔████╔██║███████║██╔██╗ ██║██║   ██║   ║
║    ██║   ██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║   ║
║    ██║   ██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝   ║
║    ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝    ║
║                                                            ║
║ ██╗   ██╗ █████╗ ███████╗ ██████╗ ███████╗                ║
║ ██║   ██║██╔══██╗██╔════╝██╔═══██╗██╔════╝                ║
║ ██║   ██║███████║███████╗██║   ██║███████╗                ║
║ ╚██╗ ██╔╝██╔══██║╚════██║██║   ██║╚════██║                ║
║  ╚████╔╝ ██║  ██║███████║╚██████╔╝███████║                ║
║   ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝                ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║   [1]  Vaso de 9oz                                        ║
║                                                            ║
║        ✔ Base                                              ║
║        ✔ Crema de la casa                                  ║
║        ✔ 1 Salsa                                            ║
║        ✔ 2 Toppings                                         ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║   [2]  Vaso de 12oz                                       ║
║                                                            ║
║        ✔ Base                                              ║
║        ✔ Crema de la casa                                  ║
║        ✔ 1 Salsa                                            ║
║        ✔ 3 Toppings                                         ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║   [3]  Vaso de 16oz                                       ║
║                                                            ║
║        ✔ Base                                              ║
║        ✔ Crema de la casa                                  ║
║        ✔ 1 Salsa                                            ║
║        ✔ 4 Toppings                                         ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║   [4]  Vaso de 24oz                                       ║
║                                                            ║
║        ✔ Base                                              ║
║        ✔ Crema de la casa                                  ║
║        ✔ 1 Salsa                                            ║
║        ✔ 3 Toppings                                         ║
║        ✔ 1 Bola de helado                                   ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║          Selecciona el tamaño de vaso deseado             ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""")
    
    op_vasos = int(input(
        "Ingrese el número de opcion del tamaño de vaso que desea ordenar: "
    ))

    if op_vasos == 1:
        nueveoz()

    elif op_vasos == 2:
        doceoz()

    elif op_vasos == 3:
        dieciseisoz()

    elif op_vasos == 4:
        veinticuatrooz()

    else:
        print("Opción no válida")

#--------------FUNCION GENERAL DE BASES------------------#
def elegir_base():

    print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║ ██████╗  █████╗ ███████╗███████╗███████╗            ║
║ ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝            ║
║ ██████╔╝███████║███████╗█████╗  ███████╗            ║
║ ██╔══██╗██╔══██║╚════██║██╔══╝  ╚════██║            ║
║ ██████╔╝██║  ██║███████║███████╗███████║            ║
║ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝            ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║        Selecciona la base que deseas                 ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║   [1]  Base de Fresa 🍓                              ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║   [2]  Base de Banano 🍌                             ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║   [3]  Base de Mango 🥭                              ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║   [4]  Base Mixta                                    ║
║        🍓 Fresa                                      ║
║        🍌 Banano                                     ║
║        🥭 Mango                                      ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║           Fraga Lover - TuOrden                      ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")

    op_base = int(input(
        "Ingrese el número de base que deseas: "
    ))

    if op_base == 1:
        return "Base de Fresa"

    elif op_base == 2:
        return "Base de Banano"

    elif op_base == 3:
        return "Base de Mango"

    elif op_base == 4:
        return "Base Mixta"

    else:
        print("Opción no válida")
        return "Sin base"

#--------------FUNCION GENERAL DE SABORES DE HELADO-----#
def elegir_helado():

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║ ██╗  ██╗███████╗██╗      █████╗ ██████╗  ██████╗        ║
║ ██║  ██║██╔════╝██║     ██╔══██╗██╔══██╗██╔═══██╗       ║
║ ███████║█████╗  ██║     ███████║██║  ██║██║   ██║       ║
║ ██╔══██║██╔══╝  ██║     ██╔══██║██║  ██║██║   ██║       ║
║ ██║  ██║███████╗███████╗██║  ██║██████╔╝╚██████╔╝       ║
║ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝        ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║           Selecciona tu sabor favorito 🍨               ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Tres leches                                       ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  Café ☕                                            ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [3]  Jumbo 🍫                                           ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [4]  Brownie 🍪                                         ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [5]  Sin helado                                        ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║               Fraga Lover - TuOrden                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    op_helado = int(input(
        "Ingrese el número del sabor de helado: "
    ))

    if op_helado == 1:
        return "Helado de tres leches"

    elif op_helado == 2:
        return "Helado de café"

    elif op_helado == 3:
        return "Helado de jumbo"

    elif op_helado == 4:
        return "Helado de brownie"

    elif op_helado == 5:
        return "Sin helado"

    else:
        return "Sin helado"


#--------------FUNCION GENERAL SALSAS--------------------#
def elegir_salsa():

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║ ███████╗ █████╗ ██╗     ███████╗ █████╗ ███████╗        ║
║ ██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝        ║
║ ███████╗███████║██║     ███████╗███████║███████╗        ║
║ ╚════██║██╔══██║██║     ╚════██║██╔══██║╚════██║        ║
║ ███████║██║  ██║███████╗███████║██║  ██║███████║        ║
║ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝        ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║            Selecciona tu salsa favorita 🍫              ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Salsa de chocolate 🍫                             ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  Salsa de arequipe 🍯                              ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [3]  Salsa de lechera 🥛                               ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [4]  Sin salsa                                         ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║               Fraga Lover - TuOrden                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    op_salsa = int(input(
        "Ingrese el número de salsa: "
    ))

    if op_salsa == 1:
        return "Salsa de chocolate"

    elif op_salsa == 2:
        return "Salsa de arequipe"

    elif op_salsa == 3:
        return "Salsa de lechera"

    elif op_salsa == 4:
        return "Sin salsa"

    else:
        print("Opción no válida")
        return "Sin salsa"


#--------------FUNCION GENERAL TOPPINGS--------------------#
def elegir_toppings(cantidad):

    lista_toppings = []

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║ ████████╗ ██████╗ ██████╗ ██████╗ ██╗███╗   ██╗  ██████╗║
║ ╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║ ██╔════╝║
║    ██║   ██║   ██║██████╔╝██████╔╝██║██╔██╗ ██║ ██║ ███╗║
║    ██║   ██║   ██║██╔═══╝ ██╔═══╝ ██║██║╚██╗██║ ██║ ╚██║  ║
║    ██║   ╚██████╔╝██║     ██║     ██║██║ ╚████║ ╚█████╔╝ ║
║    ╚═╝    ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝  ╚═════╝ ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║           Selecciona tus toppings 🧁                     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Chips blancos                                     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  Chips negros                                      ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [3]  Mini brownie de chocorramo 🍫                     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [4]  Biscolata 🍪                                      ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [5]  Sin topping                                       ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║                Fraga Lover - TuOrden                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    for i in range(cantidad):

        op_topping = int(input(f"Ingrese topping #{i+1}: "))

        if op_topping == 1:
            lista_toppings.append("Chips blancos")

        elif op_topping == 2:
            lista_toppings.append("Chips negros")

        elif op_topping == 3:
            lista_toppings.append("Mini brownie de chocorramo")

        elif op_topping == 4:
            lista_toppings.append("Biscolata")

        elif op_topping == 5:
            lista_toppings.append("Sin topping")

        else:
            print("Opción no válida")

    return lista_toppings
#----------MICHELAR-------------------#
def micheladas():

    global michelar

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║ ███╗   ███╗██╗ ██████╗██╗  ██╗███████╗██╗      █████╗   ║
║ ████╗ ████║██║██╔════╝██║  ██║██╔════╝██║     ██╔══██╗  ║
║ ██╔████╔██║██║██║     ███████║█████╗  ██║     ███████║  ║
║ ██║╚██╔╝██║██║██║     ██╔══██║██╔══╝  ██║     ██╔══██║  ║
║ ██║ ╚═╝ ██║██║╚██████╗██║  ██║███████╗███████╗██║  ██║  ║
║ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝  ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║              Selecciona cómo deseas michelar 🍹         ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Sal Limón 🍋                                      ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  Tajín 🌶️                                          ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [3]  Sin michelar                                      ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║                  Fraga Lover - TuOrden                   ║
║                                                          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    op_michelar = int(input(
        "Seleccione el numero de michelada que deseas: "
    ))

    if op_michelar == 1:

        michelar = "Michelada con Sal Limón"

    elif op_michelar == 2:

        michelar = "Michelada con Tajín"

    elif op_michelar == 3:

        michelar = "Sin michelar"

    else:

        print("Opcion no valida")
        return

    recibo()


#--------------9oz--------------------#
def nueveoz():

    global base, producto, salsa, toppings

    base = elegir_base()

    producto = "Vaso de 9oz"

    salsa = elegir_salsa()

    toppings = elegir_toppings(2)

    recibo()


#--------------12oz--------------------#
def doceoz():

    global base, producto, salsa, toppings

    base = elegir_base()

    producto = "Vaso de 12oz"

    salsa = elegir_salsa()

    toppings = elegir_toppings(3)

    recibo()


#--------------16oz--------------------#
def dieciseisoz():

    global base, producto, salsa, toppings

    base = elegir_base()

    producto = "Vaso de 16oz"

    salsa = elegir_salsa()

    toppings = elegir_toppings(4)

    recibo()


#--------------24oz--------------------#
def veinticuatrooz():

    global base, producto, salsa, toppings, helado
    

    base = elegir_base()

    producto = "Vaso de 24oz"

    salsa = elegir_salsa()

    toppings = elegir_toppings(3)

    helado = elegir_helado()

    recibo()


#---------Bowls------------#
def bowls():

    global producto
   
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║ ██████╗  ██████╗ ██╗    ██╗██╗     ███████╗             ║
║ ██╔══██╗██╔═══██╗██║    ██║██║     ██╔════╝             ║
║ ██████╔╝██║   ██║██║ █╗ ██║██║     ███████╗             ║
║ ██╔══██╗██║   ██║██║███╗██║██║     ╚════██║             ║
║ ██████╔╝╚██████╔╝╚███╔███╔╝███████╗███████║             ║
║ ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝             ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║         Selecciona el bowl que deseas 🥣                ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Bowl de frutas 🍓🥭🥝                            ║
║                                                          ║
║        ✔ Fresa                                           ║
║        ✔ Mango                                           ║
║        ✔ Manzana verde                                   ║
║        ✔ Kiwi                                            ║
║        ✔ Crema de la casa                                ║
║        ✔ Queso                                            ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  ChocoBowl 🍫                                      ║
║                                                          ║
║        ✔ Fresa                                           ║
║        ✔ Crema de la casa                                ║
║        ✔ Cobertura de chocolate                          ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║                 Fraga Lover - TuOrden                    ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    op_bowls = int(input("Ingrese el número del bowl que desea ordenar: "))

    if op_bowls == 1:

        producto = "Bowl de frutas"
    
    elif op_bowls == 2:

        producto = "ChocoBowl"
        
    else:

        print("Opción no válida")
        return

    recibo()


#---------Sodas micheladas------------#
def sodas_micheladas():

    global producto

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║ ███████╗ ██████╗ ██████╗  █████╗ ███████╗               ║
║ ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝               ║
║ ███████╗██║   ██║██║  ██║███████║███████╗               ║
║ ╚════██║██║   ██║██║  ██║██╔══██║╚════██║               ║
║ ███████║╚██████╔╝██████╔╝██║  ██║███████║               ║
║ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝               ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║              Selecciona tu soda 🍹                       ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Soda de cereza 🍒                                 ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  Soda de frutos verdes 🍏                          ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [3]  Soda de maracuyá 🥭                               ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║     Las sodas pueden michelarse con:                     ║
║                                                          ║
║        ✔ Sal Limón 🍋                                   ║
║        ✔ Tajín 🌶️                                       ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║               Fraga Lover - TuOrden                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    op_sodas = int(input("Ingrese el número de la soda michelada que desea ordenar: "))

    if op_sodas == 1:

        producto = "Soda de cereza"

    elif op_sodas == 2:

        producto = "Soda de frutos verdes"

    elif op_sodas == 3:

        producto = "Soda de maracuyá"

    else:

        print("Opción no válida")
        return

    micheladas()


#---------Otros productos------------#
def otros_productos():

    global base, helado, producto, salsa, toppings
   
    toppings.clear()

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  ██████╗ ████████╗██████╗  ██████╗ ███████╗             ║
║ ██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝             ║
║ ██║   ██║   ██║   ██████╔╝██║   ██║███████╗             ║
║ ██║   ██║   ██║   ██╔══██╗██║   ██║╚════██║             ║
║ ╚██████╔╝   ██║   ██║  ██║╚██████╔╝███████║             ║
║  ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝             ║
║                                                          ║
║ ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗
║ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝
║ ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   
║ ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   
║ ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   
║ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝   
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║          Selecciona el producto deseado 🍓              ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Maracucrema 🥭                                    ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  Chocotentación 🍫                                 ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [3]  Chocoloco 🍨                                      ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [4]  Fresas con chocolate 🍓🍫                         ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║               Fraga Lover - TuOrden                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")
    op_productos = int(input("Ingrese el número del producto que desea ordenar: "))

    if op_productos == 1:

        producto = "Maracucrema"

    elif op_productos == 2:

        producto = "Chocotentación"

    elif op_productos == 3:

        base = elegir_base()

        producto = "Chocoloco"

        helado = elegir_helado()

        salsa = elegir_salsa()

        toppings = elegir_toppings(1)

    elif op_productos == 4:

        producto = "Fresas con chocolate"

        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  ██████╗ ██████╗ ██████╗ ███████╗██████╗                ║
║ ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗               ║
║ ██║     ██║   ██║██████╔╝█████╗  ██████╔╝               ║
║ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗               ║
║ ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║               ║
║  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝               ║
║                                                          ║
║ ████████╗██╗   ██╗██████╗  █████╗                       ║
║ ╚══██╔══╝██║   ██║██╔══██╗██╔══██╗                      ║
║    ██║   ██║   ██║██████╔╝███████║                      ║
║    ██║   ██║   ██║██╔══██╗██╔══██║                      ║
║    ██║   ╚██████╔╝██║  ██║██║  ██║                      ║
║    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                      ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║         Selecciona tu cobertura favorita 🍫             ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1]  Chocolate negro 🍫                                ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [2]  Chocolate blanco 🤍                               ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [3]  Mixto 🍫🤍                                         ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║               Fraga Lover - TuOrden                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

        cobertura = int(input("Seleccione cobertura: "))

        if cobertura == 1:
            salsa = "Chocolate negro"

        elif cobertura == 2:
            salsa = "Chocolate blanco"

        elif cobertura == 3:
            salsa = "Mixto"


        else:
 
         print("Opción no válida")
         return

    recibo()
#---------------------------RECIBO--------------------------#
def recibo():
    global base, producto, salsa, toppings, michelar, helado

    print("--- INGRESO DE DATOS ---")
    nombreusu = input("Ingresa tu nombre: ")
    estadodelpedido = input("¿Deseas domicilio (30min) o recoger?: ").strip().lower()

    direccion, barrio, numero, tiemporecogida = "", "", "", ""

    if estadodelpedido == "domicilio":
        direccion = input("Ingresa tu dirección: ")
        barrio = input("Ingresa tu barrio: ")
        numero = input("Ingresa tu número telefónico: ")
    elif estadodelpedido == "recoger":
        tiemporecogida = input("¿En cuanto pasas por el?: ")
    else:
        print("❌ Opción no válida")
        return
 #----Estructura de la comanda--------#
    ticket = "\n" + "="*32 + "\n"
    ticket += "      FRAGA LOVER - TUORDEN      \n"
    ticket += "="*32 + "\n"
    ticket += f"CLIENTE: {nombreusu}\n"
    ticket += f"PRODUCTO: {producto}\n"
    ticket += f"BASE: {base}\n"
    ticket += f"SALSA: {salsa}\n"
    ticket += f"HELADO: {helado}\n"
    ticket += f"MICHELADA: {michelar}\n"
    ticket += "TOPPINGS:\n"

    if len(toppings) > 0:
        for topping in toppings:
            ticket += f"  - {topping}\n"
    else:
        ticket += "  - Sin toppings\n"

    ticket += "-"*32 + "\n"
    if estadodelpedido == "domicilio":
        ticket += "TIPO: Domicilio\n"
        ticket += f"DIRECCION: {direccion}\nBARRIO: {barrio}\nCEL: {numero}\n"
    else:
        ticket += "TIPO: Recoger en tienda\n"
        ticket += f"RECOGE EN: {tiemporecogida}\n"
    
    ticket += "="*32 + "\n"
    ticket += "     Fraga Lover - TuOrden      \n"
    ticket += "="*32 + "\n\n\n" #

    #
    comando_corte = b'\x1d\x56\x42\x00' 

    # --- Envío a la impresora ---
    try:
        nombre_impresora = "impresoraPrueba" 
        hPrinter = win32print.OpenPrinter(nombre_impresora)
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Ticket de Venta", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        

        win32print.WritePrinter(hPrinter, ticket.encode('cp1252') + comando_corte)
        
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
        win32print.ClosePrinter(hPrinter)
        print("\n✅ ¡Ticket impreso y cortado correctamente!")
    
    except Exception as e:
        print(f"\n❌ Error al conectar con la impresora: {e}")
        print("Asegúrate de que la impresora esté conectada y que el nombre sea 'impresoraPrueba'")


def menu():

    while True:
        
        print(f"""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   ███████╗██████╗  █████╗  ██████╗  █████╗          ║
║   ██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔══██╗         ║
║   █████╗  ██████╔╝███████║██║  ███╗███████║         ║
║   ██╔══╝  ██╔══██╗██╔══██║██║   ██║██╔══██║         ║
║   ██║     ██║  ██║██║  ██║╚██████╔╝██║  ██║         ║
║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝         ║
║                                                      ║
║                                                      ║
║         ██╗      ██████╗ ██╗   ██╗███████╗██████╗    ║
║         ██║     ██╔═══██╗██║   ██║██╔════╝██╔══██╗   ║
║         ██║     ██║   ██║██║   ██║█████╗  ██████╔╝   ║
║         ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██    ║
║         ███████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║   ║
║         ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝   ║  
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║              SISTEMA DE PEDIDOS - TuOrden            ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║     [1]   Tamaño de vasos                            ║
║                                                      ║
║     [2]   Bowls                                      ║
║                                                      ║
║     [3]   Sodas micheladas                           ║
║                                                      ║
║     [4]   Otros productos                            ║
║                                                      ║
║     [5]   Salir                                      ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║    Selecciona el numero de opción para continuar     ║
╚══════════════════════════════════════════════════════╝
""")

        op_menu = int(input("Ingrese la opcion: "))

        if op_menu == 1:
            tamano_vasos()

        elif op_menu == 2:
            bowls()

        elif op_menu == 3:
            sodas_micheladas()

        elif op_menu == 4:
            otros_productos()

        elif op_menu == 5:
            print("Gracias por usar TuOrden. Más rápido, más fácil")
            break

        else:
            print("Opción no válida")


#---------Ejecutar programa------------#
menu()