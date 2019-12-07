import ipywidgets as widgets

def Requerimientos():
    Req = widgets.Accordion(children=[widgets.FloatText(value=0.41, disabled=False),
                                      widgets.FloatText(value=2),
                                      widgets.FloatText(value=0.1),
                                      widgets.FloatText(value=0.2),
                                      widgets.FloatText(value=0.2)])
    Req.set_title(0, 'h [m]')
    Req.set_title(1, 'l [m]')
    Req.set_title(2, 'D [m]')
    Req.set_title(3, 'Ox [m]')
    Req.set_title(4, 'Oy [m]')
    return Req

def Esp():
    Req = widgets.Accordion(children=[widgets.FloatText(value=4.0),
                                      widgets.FloatText(value=0.001),
                                      widgets.FloatText(value=997),
                                      widgets.FloatText(value=0.5),
                                      widgets.FloatText(value=0.0005)])
    Req.set_title(0, 'Constante del flujo de entrada')
    Req.set_title(1, 'Viscosidad')
    Req.set_title(2, 'Densidad [kg/m3]')
    Req.set_title(3, 'Tiempo final [s]')
    Req.set_title(4, 'Diferencial de tiempo [s]')
    return Req

def Datos():
    Req = Requerimientos()
    E = Esp()
    maximo = widgets.FloatText(value=0.08)
    tab = widgets.Tab()
    tab.children = [Req, E, maximo]
    tab.set_title(0, 'Geometría')
    tab.set_title(1, 'Fluido')
    tab.set_title(2, 'Malla')
    return tab
