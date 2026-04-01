import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("Error: El inventario está vacío. No hay nada que guardar.")
        return

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'precio', 'cantidad']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            if incluir_header:
                escritor.writeheader()
            
            # Solo guardamos los campos necesarios (sin el ID generado en ejecución)
            for p in inventario:
                escritor.writerow({
                    'nombre': p['nombre'],
                    'precio': p['precio'],
                    'cantidad': p['cantidad']
                })
        print(f"✅ Inventario guardado exitosamente en: {ruta}")
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{ruta}'. Verifica que el archivo no esté abierto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar: {e}")

def cargar_csv(ruta):
    productos_cargados = []
    filas_invalidas = 0
    
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            # Validar encabezado
            if not lector.fieldnames or set(['nombre', 'precio', 'cantidad']) > set(lector.fieldnames):
                print("Error: El archivo no tiene el formato de encabezado válido (nombre, precio, cantidad).")
                return None, 0

            for fila in lector:
                try:
                    # Validar 3 columnas
                    if len(fila) != 3:
                        raise ValueError("Número de columnas incorrecto")
                    
                    nombre = fila['nombre'].strip().lower()
                    precio = float(fila['precio'])
                    cantidad = int(fila['cantidad'])
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos no permitidos")
                    
                    productos_cargados.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except (ValueError, TypeError, KeyError):
                    filas_invalidas += 1
                    
        return productos_cargados, filas_invalidas

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
    except UnicodeDecodeError:
        print(f"Error: Problema de codificación al leer el archivo.")
    except Exception as e:
        print(f"Error genérico al cargar: {e}")
    
    return None, filas_invalidas
  
