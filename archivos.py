import csv
import os

# ------- Funcion guardar_csv -------

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en un archivo CSV (inventario.csv) - sobrescribe el archivo si ya existe.
    
    Args:
        inventario: Lista de productos a guardar.
        ruta (str): Ruta del archivo CSV donde guardar.
        incluir_header (bool): Si incluir encabezados en el CSV. Por defecto es True.
    """
    # Validacion de inventario vacio
    if not inventario:
        print("Error: El inventario está vacío. No hay nada que guardar.")
        return

    try:
        # Crear el directorio si no existe
        directorio = os.path.dirname(ruta) #os.path.dirname devuelve la parte del directorio de la ruta, si es una ruta sin directorio devuelve cadena vacía
        if directorio and not os.path.exists(directorio): # Si hay un directorio especificado y no existe, lo crea
            os.makedirs(directorio, exist_ok=True)
        
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo: #w=modo escritura (sobrescribe si el archivo existe), newline='' para evitar líneas en blanco adicionales, utf-8 para evitar problemas de codificación, with open para asegurar cierre del archivo
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


# ------- Funcion cargar_csv -------

def cargar_csv(ruta):
    """Carga productos desde un archivo CSV.
    
    Argumentos:
        ruta (str): Ruta del archivo CSV a cargar.
    
    Retorna:
        Una tupla con dos elementos:
        - Lista de productos cargados (cada producto es un diccionario con nombre, precio y cantidad).
        - Número de filas inválidas encontradas durante la carga.
    """
    productos_cargados = []
    filas_invalidas = 0
    
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo: #r=modo lectura, utf-8 para evitar problemas de codificación, with open para asegurar cierre del archivo
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
  
