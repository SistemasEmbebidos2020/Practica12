def obtener_temperatura():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as archivo:
            temp_raw = archivo.read()
        temp_c = float(temp_raw) / 1000.0
        return temp_c
    except FileNotFoundError:
        print("El archivo de temperatura no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
