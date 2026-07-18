# =============================
# SISTEMA TIENDA ROPA 
# =============================

prendas = {}
bodega = {}

# =======================
# VALIDACIONES
# =======================

def validar_codigo(codigo):
    return codigo.strip() != "" and codigo.upper() not in prendas

def validar_texto(txt):
    return txt.strip() != ""

def validar_unisex(valor):
    return valor.lower() == "s" or valor.lower() == "n"

def validar_precio(p):
    return p > 0

def validar_unidades(u):
    return u >= 0


# =========================
# FUNCIONES PRINCIPALES
# =========================

def unidades_categoria(categoria):
    total = 0

    for codigo in prendas:
        if prendas[codigo][1].lower() == categoria.lower():
            total += bodega[codigo][1]

    print("Total unidades:", total)


def busqueda_precio(p_min, p_max):
    lista = []

    for codigo in bodega:
        precio = bodega[codigo][0]
        stock = bodega[codigo][1]

        if precio >= p_min and precio <= p_max and stock > 0:
            nombre = prendas[codigo][0]
            lista.append(nombre + "--" + codigo)

    if len(lista) == 0:
        print("No hay prendas en ese rango de precios.")
    else:
        lista.sort()
        print("Resultados:", lista)


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()

    if codigo in bodega:
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False


def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
    codigo = codigo.upper()

    if codigo in prendas:
        return False

    prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
    bodega[codigo] = [precio, unidades]

    return True


def eliminar_prenda(codigo):
    codigo = codigo.upper()

    if codigo in prendas:
        prendas.pop(codigo)
        bodega.pop(codigo)
        return True
    else:
        return False


# ==================
# MENU PRINCIPAL
# ==================

while True:
    print("\n===== MENU =====")
    print("1. Unidades por categoria")
    print("2. Buscar por precio")
    print("3. Actualizar precio")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")

    try:
        op = int(input("Seleccione opcion: "))

        if op == 1:
            categoria = input("Ingrese categoria: ")
            unidades_categoria(categoria)

        elif op == 2:
            try:
                p_min = int(input("Precio minimo: "))
                p_max = int(input("Precio maximo: "))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("Debe ingresar valores enteros")

        elif op == 3:
            while True:
                codigo = input("Codigo: ")
                try:
                    nuevo = int(input("Nuevo precio: "))
                except ValueError:
                    print("Debe ser numero")
                    continue

                if actualizar_precio(codigo, nuevo):
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")

                seguir = input("¿Desea continuar (s/n)? ")
                if seguir.lower() == "n":
                    break

        elif op == 4:
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            categoria = input("Categoria: ")
            talla = input("Talla: ")
            color = input("Color: ")
            material = input("Material: ")
            unisex = input("¿Es unisex (s/n)? ")

            if not (validar_codigo(codigo) and validar_texto(nombre) and validar_texto(categoria)
                    and validar_texto(talla) and validar_texto(color)
                    and validar_texto(material) and validar_unisex(unisex)):
                print("Error en datos")
                continue

            try:
                precio = int(input("Precio: "))
                unidades = int(input("Unidades: "))
            except ValueError:
                print("Error numerico")
                continue

            if not validar_precio(precio) or not validar_unidades(unidades):
                print("Valores invalidos")
                continue

            es_unisex = True if unisex.lower() == "s" else False

            if agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
                print("Prenda agregada")
            else:
                print("El codigo ya existe")

        elif op == 5:
            codigo = input("Codigo: ")

            if eliminar_prenda(codigo):
                print("Prenda eliminada")
            else:
                print("El codigo no existe")

        elif op == 6:
            print("Programa finalizado")
            break

        else:
            print("Debe seleccionar una opcion valida")

    except ValueError:
        print("Debe ingresar un numero")