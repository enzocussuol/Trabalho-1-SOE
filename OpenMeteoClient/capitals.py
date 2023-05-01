class Location():
    def __init__(self,latitude,longitude,name,cod = ""):
        self.longitude = longitude
        self.latitude = latitude
        self.name = name
        self.cod = cod

    def set_code(self,cod):
        self.cod = cod

    def get_long(self):
        return self.longitude
    def get_lat(self):
        return self.latitude
    def get_name(self):
        return self.name
        
    def get_location(self):
        return (self.latitude,self.longitude,self.name)
    
    def __repr__(self):
        return self.name

CAPITALS = {
    "BR-AC": Location( -8.77, -70.55, "Rio Branco"),
    "BR-AL": Location( -9.71, -35.73, "Maceio"),
    "BR-AM": Location( -3.07, -61.66, "Manaus"), 
    "BR-AP": Location(  1.41, -51.77, "Macapa"),
    "BR-BA": Location(-12.96, -38.51, "Salvador"),
    "BR-CE": Location( -3.71, -38.54, "Fortaleza"),
    "BR-DF": Location(-15.83, -47.86, "Brasilia"),
    "BR-ES": Location(-19.19, -40.34, "Vitoria"),
    "BR-GO": Location(-16.64, -49.31, "Goiania"),
    "BR-MA": Location( -2.55, -44.30, "Sao Luis"),
    "BR-MT": Location(-12.64, -55.42, "Cuiaba"),
    "BR-MS": Location(-20.51, -54.54, "Campo Grande"),
    "BR-MG": Location(-18.10, -44.38, "Belo Horizonte"),
    "BR-PA": Location( -5.53, -52.29, "Belém"),
    "BR-PB": Location( -7.06, -35.55, "João Pessoa"),
    "BR-PR": Location(-24.89, -51.55, "Curitiba"),
    "BR-PE": Location( -8.28, -35.07, "Recife"),
    "BR-PI": Location( -8.28, -43.68, "Teresina"),
    "BR-RJ": Location(-22.84, -43.15, "Rio de Janeiro"),
    "BR-RN": Location( -5.22, -36.52, "Natal"),
    "BR-RO": Location(-11.22, -62.80, "Porto Velho"),
    "BR-RS": Location(-30.01, -51.22, "Porto Alegre"),
    "BR-RR": Location(  1.89, -61.22, "Boa Vista"),
    "BR-SC": Location(-27.33, -49.44, "Florianópolis"), 
    "BR-SE": Location(-10.90, -37.07, "Aracaju"),
    "BR-SP": Location(-23.55, -46.64, "São Paulo"), 
    "BR-TO": Location(-10.25, -48.25, "Palmas")
}