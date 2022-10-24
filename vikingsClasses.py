from configparser import NoOptionError


class Soldier:
    
    def __init__(self,salud,fuerza):
        
        self.salud = salud
        self.fuerza = fuerza

    def get_salud(self):
        return self.salud


    def get_fuerza(self):
        return self.fuerza

    def recibir_daño(self, daño):
        self.salud = self.salud - daño

# Viking


class Viking(Soldier):
    def __init__(self,nombre):
        self.nombre= nombre
        super().__init__()
        
    def recibir_daño(self, daño):
        self.salud = self.salud - daño
        if self.salud <= 0:
            print(self.nombre, " ha muerto en combate")
        else:
            print(self.nombre, " ha recibido", daño, " puntos  de daño")
    
    def battle_cry(self):
        print("Odin Owns You All!")



class Saxon:
    def __init__(self):
        super().__init__()

    def recibir_daño(self, daño):
        self.salud = self.salud - daño
        if self.salud <= 0:
            print("Un Saxon ha muerto en combate")
        else:
            print("Un Saxon ha recibido", daño, " puntos  de daño")


class War:
    def __init__(self):
        self.vikingos=[]
        self.saxon=[]
        self.ataque_vikingo=None
        self.ataque_saxon=None
        self.estado=None

    def set_añadir_vikingo(self, vikingo):
        self.vikingos.append(vikingo)

    def set_añadir_saxon(self, saxon):
        self.saxon.append(saxon)

    def set_ataque_vikingo(self, vikingo):
        


