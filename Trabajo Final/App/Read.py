import ipywidgets as widgets

def Read(raw):
    datos = {
        'Geo':{},
        'Fluido':{}
    }
    cont = 0
    for tipo in datos:
        suma = 0
        while True:
            try:
                datos[tipo][raw.children[cont].get_title(suma)] = raw.children[cont].children[suma].value
                suma += 1
            except:
                break
        cont += 1
    return datos