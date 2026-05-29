import win32print

# Nombre de la impresora tal como la configuraste en Windows
nombre_impresora = "impresoraPrueba" 

try:
    # 1. Intentar conectar con la impresora
    hPrinter = win32print.OpenPrinter(nombre_impresora)
    
    # 2. Iniciar el trabajo de impresión
    # "RAW" indica que enviamos los datos directamente sin procesar
    hJob = win32print.StartDocPrinter(hPrinter, 1, ("Prueba de Impresión", None, "RAW"))
    win32print.StartPagePrinter(hPrinter)

    # 3. Contenido del ticket
    # Puedes usar '\n' para saltos de línea
    ticket = "¡Hola Mundo!\n"
    ticket += "Imprimiendo desde Python en VS Code.\n"
    ticket += "La configuración es exitosa.\n\n\n"
    
    # Enviar al buffer de la impresora
    win32print.WritePrinter(hPrinter, ticket.encode('utf-8'))

    # 4. Finalizar y cerrar
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
    win32print.ClosePrinter(hPrinter)
    
    print("¡Éxito! El ticket debería estar saliendo de la impresora ahora mismo.")

except Exception as e:
    print(f"--- Ocurrió un error ---")
    print(f"Error: {e}")
    print("Verifica:")
    print("1. Que el cable USB esté conectado al computador.")
    print("2. Que el nombre 'impresoraPrueba' coincida exactamente con el de tu configuración de Windows.")