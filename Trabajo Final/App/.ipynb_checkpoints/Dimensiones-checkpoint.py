import math
class Volumenes():
    def __init__(self, data):
        #Volúmenes en m3
        V_AD = self.AD(data['Req']['Relación másica AD - MV'], 
                       data['Req']['Capacidad [kg/bache]'], 
                       data['Esp']['Densidad del agente dispersante [kg/m3]'])
        V_MV = data['Req']['Capacidad [kg/bache]']/data['Esp']['Densidad del material vegetal [kg/m3]']
        V_Tb, mult = self.Bolas(V_AD, V_MV, data['Esp']['Relación volumétrica de carga del molino [%]'],
                          data['Esp']['Volumen porcentual de las bolas (con respecto al total) [%]'])
        V = mult*(V_AD+V_MV+V_Tb)
        
        #Mostrar resultados...
        self.resul = {
            'V_AD': V_AD,
            'V_MV': V_MV,
            'V_Tb': V_Tb,
            'V': V
        }
        self.Vol = {
            'Tipo': ['$V_{AD}$', '$V_{MV}$', '$V_{Tb}$', '$V_{T}$'],
            'Valor $[L]$': [round(V_AD*1000,2), round(V_MV*1000,2), round(V_Tb*1000,2), round(V*1000,2)]
        }
    
    def __call__(self):
        return self.resul, self.Vol
    
    def Bolas(self, AD, MV, pcarga, pbolas):
        """
            AD - Volumen ocupado por el agente dispersante
            MV - Volumen ocupado por el material vegetal
            pcarga - Porcentaje de carga del molino
            pbolas - Volumen porcentual de las bolas (con respecto al total)
            V = mult*(AD+MV+Tb)
        """
        pcarga = pcarga/100
        pbolas = pbolas/100
        mult = 1/pcarga
        return ((mult*pbolas)/(1-mult*pbolas))*(AD+MV), mult
    
    def AD(self, Rel, Cap, rho):
        m = Cap*Rel    #kg
        return m/rho
    
def dim(V, rel):
    mult = math.pi*rel/4
    D = ((1/mult)*V)**(1/3)
    L = rel*D
    return D,L