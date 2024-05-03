class Jel: 
    def __init__(self, ora, perc, mp, x, y): 
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.x = x
        self.y = y

    def __str__(self):
        return f"Óra: {self.ora} \nPerc: {self.perc} \nMásodperc: {self.mp} \nX: {self.x} \Y: {self.y}" 
        
f = open("jel.txt", "rt", encoding="utf-8")      

lista = []  

for sor in f:
    sor = sor.strip().split(' ')
lista.append(Jel(sor[0],sor[1],sor[2],sor[3],sor[4]))
print("2. feladat: ")

bemenet = int(input("Kérem egy jel sorszámát: ")) -1
print(f'x={lista[bemenet].x} y={lista[bemenet].y}')
f.close()

def eltelt():
