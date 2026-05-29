# =====================================================
#                  TuOrden - v2.0
#         Sistema de Pedidos y Caja Registradora
#              Fraga Lover - Roldanillo
# =====================================================

import win32print
import sqlite3
from datetime import datetime

# ----------- BASE DE DATOS -----------
def iniciar_base_de_datos():
    conn = sqlite3.connect("tuorden.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha       TEXT,
            cliente     TEXT,
            producto    TEXT,
            base        TEXT,
            salsa       TEXT,
            helado      TEXT,
            michelada   TEXT,
            toppings    TEXT,
            tipo        TEXT,
            direccion   TEXT,
            barrio      TEXT,
            telefono    TEXT,
            recoge_en   TEXT,
            total       REAL,
            estado      TEXT DEFAULT 'pendiente',
            metodo_pago TEXT,
            hora_pago   TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_pedido(cliente, producto, base, salsa, helado, michelada,
                   toppings_lista, tipo, direccion, barrio, telefono,
                   recoge_en, total):
    conn = sqlite3.connect("tuorden.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pedidos
        (fecha, cliente, producto, base, salsa, helado, michelada,
         toppings, tipo, direccion, barrio, telefono, recoge_en, total, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pendiente')
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        cliente, producto, base, salsa, helado, michelada,
        ", ".join(toppings_lista) if toppings_lista else "Sin toppings",
        tipo, direccion, barrio, telefono, recoge_en, total
    ))
    conn.commit()
    conn.close()
    print("✅ Pedido guardado en el sistema.")

def obtener_pedidos_pendientes():
    conn = sqlite3.connect("tuorden.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, fecha, cliente, producto, total
        FROM pedidos
        WHERE estado = 'pendiente'
        ORDER BY id ASC
    """)
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

def obtener_pedido_por_id(pedido_id):
    conn = sqlite3.connect("tuorden.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,))
    pedido = cursor.fetchone()
    conn.close()
    return pedido

def marcar_como_pagado(pedido_id, metodo_pago):
    conn = sqlite3.connect("tuorden.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE pedidos
        SET estado = 'pagado', metodo_pago = ?, hora_pago = ?
        WHERE id = ?
    """, (metodo_pago, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), pedido_id))
    conn.commit()
    conn.close()

# ----------- PRECIOS -----------
PRECIOS = {
    "Vaso de 9oz":          11000,
    "Vaso de 12oz":         14000,
    "Vaso de 16oz":         17000,
    "Vaso de 24oz":         25000,
    "Soda de cereza":       13000,
    "Soda de frutos verdes":13000,
    "Soda de maracuyá":     13000,
    "Maracucrema":          15000,
    "Bowl de frutas":       17000,
    "ChocoBowl":            15000,
    "Chocotentación":       16000,
    "Chocoloco":            13000,
    "Fresas con chocolate": 14000,
}
COSTO_DOMICILIO = 2500

# ----------- VARIABLES GLOBALES -----------
producto  = ""
salsa     = ""
toppings  = []
helado    = ""
michelar  = ""
base      = ""

# =====================================================
#                  IMPRESORA
# =====================================================
def imprimir_ticket(contenido):
    comando_corte = b'\x1d\x56\x42\x00'
    try:
        nombre_impresora = "impresoraPrueba"
        hPrinter = win32print.OpenPrinter(nombre_impresora)
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Ticket", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, contenido.encode('cp1252') + comando_corte)
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
        win32print.ClosePrinter(hPrinter)
        print("\n✅ Ticket impreso correctamente.")
    except Exception as e:
        print(f"\n❌ Error con la impresora: {e}")

# =====================================================
#               MÓDULO TOMA DE PEDIDOS
# =====================================================
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
╠════════════════════════════════════════════════════════════╣
║  [1]  Vaso 9oz  - $11.000   ✔ Base ✔ 1 Salsa ✔ 2 Toppings ║
║  [2]  Vaso 12oz - $14.000   ✔ Base ✔ 1 Salsa ✔ 3 Toppings ║
║  [3]  Vaso 16oz - $17.000   ✔ Base ✔ 1 Salsa ✔ 4 Toppings ║
║  [4]  Vaso 24oz - $25.000   ✔ Base ✔ 1 Salsa ✔ 3 Toppings ║
║                             ✔ 1 Bola de helado             ║
╚════════════════════════════════════════════════════════════╝
""")
    op = int(input("Selecciona el tamaño: "))
    if   op == 1: nueveoz()
    elif op == 2: doceoz()
    elif op == 3: dieciseisoz()
    elif op == 4: veinticuatrooz()
    else: print("Opción no válida")

def elegir_base():
    print("""
╔══════════════════════════════════════════════════════╗
║           Selecciona la base que deseas              ║
╠══════════════════════════════════════════════════════╣
║   [1]  Base de Fresa 🍓                              ║
║   [2]  Base de Banano 🍌                             ║
║   [3]  Base de Mango 🥭                              ║
║   [4]  Base Mixta  🍓🍌🥭                            ║
╚══════════════════════════════════════════════════════╝
""")
    op = int(input("Ingresa el número de base: "))
    opciones = {1: "Base de Fresa", 2: "Base de Banano",
                3: "Base de Mango", 4: "Base Mixta"}
    return opciones.get(op, "Sin base")

def elegir_helado():
    print("""
╔══════════════════════════════════════════════════════════╗
║           Selecciona tu sabor favorito 🍨               ║
╠══════════════════════════════════════════════════════════╣
║   [1]  Tres leches  [2]  Café ☕                         ║
║   [3]  Jumbo 🍫     [4]  Brownie 🍪   [5]  Sin helado    ║
╚══════════════════════════════════════════════════════════╝
""")
    op = int(input("Ingresa el número del sabor: "))
    opciones = {1: "Helado de tres leches", 2: "Helado de café",
                3: "Helado de jumbo", 4: "Helado de brownie", 5: "Sin helado"}
    return opciones.get(op, "Sin helado")

def elegir_salsa():
    print("""
╔══════════════════════════════════════════════════════════╗
║            Selecciona tu salsa favorita 🍫              ║
╠══════════════════════════════════════════════════════════╣
║   [1]  Chocolate 🍫   [2]  Arequipe 🍯                   ║
║   [3]  Lechera 🥛     [4]  Sin salsa                     ║
╚══════════════════════════════════════════════════════════╝
""")
    op = int(input("Ingresa el número de salsa: "))
    opciones = {1: "Salsa de chocolate", 2: "Salsa de arequipe",
                3: "Salsa de lechera", 4: "Sin salsa"}
    return opciones.get(op, "Sin salsa")

def elegir_toppings(cantidad):
    lista = []
    print("""
╔══════════════════════════════════════════════════════════╗
║           Selecciona tus toppings 🧁                     ║
╠══════════════════════════════════════════════════════════╣
║   [1] Chips blancos        [2] Chips negros              ║
║   [3] Mini brownie 🍫      [4] Biscolata 🍪              ║
║   [5] Sin topping                                        ║
╚══════════════════════════════════════════════════════════╝
""")
    opciones = {1: "Chips blancos", 2: "Chips negros",
                3: "Mini brownie de chocorramo", 4: "Biscolata", 5: "Sin topping"}
    for i in range(cantidad):
        op = int(input(f"Topping #{i+1}: "))
        lista.append(opciones.get(op, "Sin topping"))
    return lista

def micheladas():
    global michelar
    print("""
╔══════════════════════════════════════════════════════════╗
║              ¿Cómo deseas michelar? 🍹                  ║
╠══════════════════════════════════════════════════════════╣
║   [1]  Sal Limón 🍋    [2]  Tajín 🌶️    [3]  Sin michelar║
╚══════════════════════════════════════════════════════════╝
""")
    op = int(input("Selecciona: "))
    opciones = {1: "Michelada con Sal Limón", 2: "Michelada con Tajín", 3: "Sin michelar"}
    michelar = opciones.get(op, "Sin michelar")
    recibo()

def nueveoz():
    global base, producto, salsa, toppings
    base = elegir_base(); producto = "Vaso de 9oz"
    salsa = elegir_salsa(); toppings = elegir_toppings(2)
    recibo()

def doceoz():
    global base, producto, salsa, toppings
    base = elegir_base(); producto = "Vaso de 12oz"
    salsa = elegir_salsa(); toppings = elegir_toppings(3)
    recibo()

def dieciseisoz():
    global base, producto, salsa, toppings
    base = elegir_base(); producto = "Vaso de 16oz"
    salsa = elegir_salsa(); toppings = elegir_toppings(4)
    recibo()

def veinticuatrooz():
    global base, producto, salsa, toppings, helado
    base = elegir_base(); producto = "Vaso de 24oz"
    salsa = elegir_salsa(); toppings = elegir_toppings(3)
    helado = elegir_helado(); recibo()

def bowls():
    global producto
    print("""
╔══════════════════════════════════════════════════════════╗
║         Selecciona el bowl que deseas 🥣                ║
╠══════════════════════════════════════════════════════════╣
║   [1]  Bowl de frutas 🍓🥭🥝  -  $17.000                ║
║        Fresa, Mango, Manzana, Kiwi, Crema, Queso        ║
╠══════════════════════════════════════════════════════════╣
║   [2]  ChocoBowl 🍫           -  $15.000                ║
║        Fresa, Crema, Cobertura de chocolate             ║
╚══════════════════════════════════════════════════════════╝
""")
    op = int(input("Ingresa el número del bowl: "))
    if   op == 1: producto = "Bowl de frutas"
    elif op == 2: producto = "ChocoBowl"
    else: print("Opción no válida"); return
    recibo()

def sodas_micheladas():
    global producto
    print("""
╔══════════════════════════════════════════════════════════╗
║              Selecciona tu soda 🍹  -  $13.000          ║
╠══════════════════════════════════════════════════════════╣
║   [1]  Soda de cereza 🍒                                 ║
║   [2]  Soda de frutos verdes 🍏                          ║
║   [3]  Soda de maracuyá 🥭                               ║
╚══════════════════════════════════════════════════════════╝
""")
    op = int(input("Ingresa el número de la soda: "))
    opciones = {1: "Soda de cereza", 2: "Soda de frutos verdes", 3: "Soda de maracuyá"}
    if op in opciones:
        producto = opciones[op]
        micheladas()
    else:
        print("Opción no válida")

def otros_productos():
    global base, helado, producto, salsa, toppings
    toppings.clear()
    print("""
╔══════════════════════════════════════════════════════════╗
║          Selecciona el producto deseado 🍓              ║
╠══════════════════════════════════════════════════════════╣
║   [1]  Maracucrema 🥭         -  $15.000                 ║
║   [2]  Chocotentación 🍫      -  $16.000                 ║
║   [3]  Chocoloco 🍨           -  $13.000                 ║
║   [4]  Fresas con chocolate 🍓🍫 - $14.000               ║
╚══════════════════════════════════════════════════════════╝
""")
    op = int(input("Ingresa el número del producto: "))
    if op == 1:
        producto = "Maracucrema"
    elif op == 2:
        producto = "Chocotentación"
    elif op == 3:
        base    = elegir_base()
        producto = "Chocoloco"
        helado  = elegir_helado()
        salsa   = elegir_salsa()
        toppings = elegir_toppings(1)
    elif op == 4:
        producto = "Fresas con chocolate"
        print("""
╔══════════════════════════════════════════════════════════╗
║         Selecciona tu cobertura favorita 🍫             ║
╠══════════════════════════════════════════════════════════╣
║   [1]  Chocolate negro 🍫                                ║
║   [2]  Chocolate blanco 🤍                               ║
║   [3]  Mixto 🍫🤍                                         ║
╚══════════════════════════════════════════════════════════╝
""")
        cob = int(input("Selecciona cobertura: "))
        coberturas = {1: "Chocolate negro", 2: "Chocolate blanco", 3: "Mixto"}
        salsa = coberturas.get(cob, "Sin cobertura")
    else:
        print("Opción no válida"); return
    recibo()

# =====================================================
#                     RECIBO
# =====================================================
def recibo():
    global base, producto, salsa, toppings, michelar, helado

    print("\n--- INGRESO DE DATOS ---")
    nombreusu      = input("Ingresa el nombre del cliente: ")
    estadodelpedido = input("¿Domicilio o recoger?: ").strip().lower()

    direccion = barrio = numero = tiemporecogida = ""

    if estadodelpedido == "domicilio":
        direccion      = input("Dirección: ")
        barrio         = input("Barrio: ")
        numero         = input("Teléfono: ")
    elif estadodelpedido == "recoger":
        tiemporecogida = input("¿En cuánto tiempo recoge?: ")
    else:
        print("❌ Opción no válida"); return

    # Calcular total
    precio_base   = PRECIOS.get(producto, 0)
    costo_domici  = COSTO_DOMICILIO if estadodelpedido == "domicilio" else 0
    total         = precio_base + costo_domici

    # Comanda para cocina (impresora)
    ticket  = "\n" + "="*32 + "\n"
    ticket += "    FRAGA LOVER - TUORDEN\n"
    ticket += "="*32 + "\n"
    ticket += f"CLIENTE : {nombreusu}\n"
    ticket += f"PRODUCTO: {producto}\n"
    if base:     ticket += f"BASE    : {base}\n"
    if salsa:    ticket += f"SALSA   : {salsa}\n"
    if helado:   ticket += f"HELADO  : {helado}\n"
    if michelar: ticket += f"MICHELAD: {michelar}\n"
    if toppings:
        ticket += "TOPPINGS:\n"
        for t in toppings:
            ticket += f"  - {t}\n"
    ticket += "-"*32 + "\n"
    if estadodelpedido == "domicilio":
        ticket += f"TIPO    : Domicilio (+$2.500)\n"
        ticket += f"DIR     : {direccion}\n"
        ticket += f"BARRIO  : {barrio}\n"
        ticket += f"CEL     : {numero}\n"
    else:
        ticket += f"TIPO    : Recoger en tienda\n"
        ticket += f"RECOGE  : {tiemporecogida}\n"
    ticket += "-"*32 + "\n"
    ticket += f"TOTAL   : ${total:,.0f}\n"
    ticket += "="*32 + "\n"
    ticket += "   Fraga Lover - TuOrden\n"
    ticket += "="*32 + "\n\n\n"

    imprimir_ticket(ticket)

    # Guardar en base de datos
    guardar_pedido(
        cliente    = nombreusu,
        producto   = producto,
        base       = base,
        salsa      = salsa,
        helado     = helado,
        michelada  = michelar,
        toppings_lista = toppings,
        tipo       = estadodelpedido,
        direccion  = direccion,
        barrio     = barrio,
        telefono   = numero,
        recoge_en  = tiemporecogida,
        total      = total
    )

    # Limpiar variables para el siguiente pedido
    base = salsa = helado = michelar = producto = ""
    toppings.clear()

# =====================================================
#               MÓDULO CAJERO
# =====================================================
def cajero():
    while True:
        print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   ██████╗ █████╗      ██╗███████╗██████╗  ██████╗   ║
║  ██╔════╝██╔══██╗     ██║██╔════╝██╔══██╗██╔═══██╗  ║
║  ██║     ███████║     ██║█████╗  ██████╔╝██║   ██║  ║
║  ██║     ██╔══██║██   ██║██╔══╝  ██╔══██╗██║   ██║  ║
║  ╚██████╗██║  ██║╚█████╔╝███████╗██║  ██║╚██████╔╝  ║
║   ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝   ║
║                                                      ║
║              MÓDULO DE CAJA - TuOrden                ║
╠══════════════════════════════════════════════════════╣
║   [1]  Ver pedidos pendientes                        ║
║   [2]  Cobrar un pedido                              ║
║   [3]  Volver al menú principal                      ║
╚══════════════════════════════════════════════════════╝
""")
        op = int(input("Selecciona una opción: "))

        if op == 1:
            ver_pedidos_pendientes()
        elif op == 2:
            cobrar_pedido()
        elif op == 3:
            break
        else:
            print("Opción no válida")

def ver_pedidos_pendientes():
    pedidos = obtener_pedidos_pendientes()
    if not pedidos:
        print("\n📭 No hay pedidos pendientes por cobrar.\n")
        return
    print("\n" + "="*55)
    print(f"  {'ID':<5} {'HORA':<20} {'CLIENTE':<15} {'PRODUCTO':<18} {'TOTAL':>8}")
    print("="*55)
    for p in pedidos:
        pid, fecha, cliente, prod, total = p
        hora = fecha[11:16]  # Solo HH:MM
        print(f"  #{pid:<4} {hora:<20} {cliente:<15} {prod:<18} ${total:>8,.0f}")
    print("="*55 + "\n")

def cobrar_pedido():
    pedidos = obtener_pedidos_pendientes()
    if not pedidos:
        print("\n📭 No hay pedidos pendientes por cobrar.\n")
        return

    ver_pedidos_pendientes()

    try:
        pedido_id = int(input("Ingresa el ID del pedido a cobrar: "))
    except ValueError:
        print("❌ ID no válido"); return

    pedido = obtener_pedido_por_id(pedido_id)
    if not pedido or pedido[15] != "pendiente":
        print("❌ Pedido no encontrado o ya fue cobrado."); return

    # Columnas: id(0) fecha(1) cliente(2) producto(3) base(4) salsa(5)
    #           helado(6) michelada(7) toppings(8) tipo(9) dir(10)
    #           barrio(11) tel(12) recoge(13) total(14) estado(15)
    #           metodo_pago(16) hora_pago(17)
    total = pedido[14]

    print(f"""
╔══════════════════════════════════════════════════════╗
║               RESUMEN DEL PEDIDO #{pedido[0]:<4}              ║
╠══════════════════════════════════════════════════════╣
║  Cliente : {pedido[2]:<42}║
║  Producto: {pedido[3]:<42}║
║  Tipo    : {pedido[9]:<42}║
║  Total   : ${total:<41,.0f}║
╚══════════════════════════════════════════════════════╝
""")

    print("Método de pago:")
    print("  [1]  Efectivo 💵")
    print("  [2]  Tarjeta / Datáfono 💳")
    print("  [3]  Transferencia / Nequi / Daviplata 📱")

    try:
        op_pago = int(input("Selecciona el método: "))
    except ValueError:
        print("❌ Opción no válida"); return

    metodos = {1: "Efectivo", 2: "Tarjeta/Datafono", 3: "Transferencia"}
    if op_pago not in metodos:
        print("❌ Opción no válida"); return

    metodo = metodos[op_pago]
    cambio = 0

    if op_pago == 1:  # Efectivo → calcular cambio
        try:
            recibido = float(input(f"Monto recibido ($): "))
        except ValueError:
            print("❌ Monto no válido"); return
        if recibido < total:
            print(f"❌ El monto recibido (${recibido:,.0f}) es menor al total (${total:,.0f}).")
            return
        cambio = recibido - total
        print(f"\n✅ Cambio a devolver: ${cambio:,.0f}")

    # Marcar como pagado
    marcar_como_pagado(pedido_id, metodo)

    # Imprimir recibo de pago
    imprimir_recibo_pago(pedido, metodo, cambio)
    print(f"\n✅ Pedido #{pedido_id} cobrado correctamente con {metodo}.")

def imprimir_recibo_pago(pedido, metodo_pago, cambio):
    total = pedido[14]
    recibo_txt  = "\n" + "="*32 + "\n"
    recibo_txt += "    FRAGA LOVER - TUORDEN\n"
    recibo_txt += "      RECIBO DE PAGO\n"
    recibo_txt += "="*32 + "\n"
    recibo_txt += f"Pedido  : #{pedido[0]}\n"
    recibo_txt += f"Fecha   : {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    recibo_txt += f"Cliente : {pedido[2]}\n"
    recibo_txt += f"Producto: {pedido[3]}\n"
    recibo_txt += "-"*32 + "\n"
    recibo_txt += f"TOTAL   : ${total:,.0f}\n"
    recibo_txt += f"PAGO CON: {metodo_pago}\n"
    if cambio > 0:
        recibo_txt += f"CAMBIO  : ${cambio:,.0f}\n"
    recibo_txt += "="*32 + "\n"
    recibo_txt += "  Gracias por tu visita!\n"
    recibo_txt += "  Fraga Lover - TuOrden\n"
    recibo_txt += "="*32 + "\n\n\n"
    imprimir_ticket(recibo_txt)

# =====================================================
#               MENÚ PRINCIPAL (MESERO)
# =====================================================
def menu_mesero():
    while True:
        print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   ███████╗██████╗  █████╗  ██████╗  █████╗          ║
║   ██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔══██╗         ║
║   █████╗  ██████╔╝███████║██║  ███╗███████║         ║
║   ██╔══╝  ██╔══██╗██╔══██║██║   ██║██╔══██║         ║
║   ██║     ██║  ██║██║  ██║╚██████╔╝██║  ██║         ║
║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝         ║
║                                                      ║
║              SISTEMA DE PEDIDOS - TuOrden            ║
╠══════════════════════════════════════════════════════╣
║   [1]   Tamaño de vasos                              ║
║   [2]   Bowls                                        ║
║   [3]   Sodas micheladas                             ║
║   [4]   Otros productos                              ║
║   [5]   Salir                                        ║
╚══════════════════════════════════════════════════════╝
""")
        op = int(input("Ingresa la opción: "))
        if   op == 1: tamano_vasos()
        elif op == 2: bowls()
        elif op == 3: sodas_micheladas()
        elif op == 4: otros_productos()
        elif op == 5:
            print("Hasta luego. Más rápido, más fácil — TuOrden"); break
        else:
            print("Opción no válida")

# =====================================================
#                  LOGIN
# =====================================================
def login():
    print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║  ████████╗██╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗║
║  ╚══██╔══╝██║   ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝║
║     ██║   ██║   ██║██║   ██║██████╔╝██║  ██║█████╗  ║
║     ██║   ██║   ██║██║   ██║██╔══██╗██║  ██║██╔══╝  ║
║     ██║   ╚██████╔╝╚██████╔╝██║  ██║██████╔╝███████╗║
║     ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║         Bienvenido a TuOrden - Fraga Lover           ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║   [1]   Mesero  🛎️   (Tomar pedidos)                 ║
║                                                      ║
║   [2]   Cajero  💰   (Caja registradora)             ║
║                                                      ║
║   [3]   Salir                                        ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")
    op = int(input("Selecciona tu rol: "))
    if   op == 1: menu_mesero()
    elif op == 2: cajero()
    elif op == 3: print("Hasta luego."); exit()
    else: print("Opción no válida"); login()

# =====================================================
#                  ARRANQUE
# =====================================================
iniciar_base_de_datos()
login()