import re
from io import open 

class Db():

    def __init__(self, filename):
        self.filename = filename
    
    def find_id_in_db(self, cedula):
        with open(self.filename, 'r') as dbfile:
            row = 0
            lines = dbfile.readlines()
            for line in lines:
                columns = line.split(',')
                if cedula==columns[0]:
                    return row
                row += 1
            return False
            row = -1
            return row

    def tiene_cantidad_notas_minimas(self, row):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:7]
        cantidad_minima = 3
        print(grades)
        if len(grades) <= cantidad_minima:
            return False
        for i in range(cantidad_minima):
            try:
                int(grades[i])
            except Exception as error:
                print(error)
                return False
        return True
    
    def calcula_promedio(self, row):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            notamax = sorted(grades[0:4])
            notas_altas = notamax[1:4]
            total = 0
            for nota_alta in notas_altas:
                total += int(nota_alta)
            promedio_1 = total/3
        return promedio_1
    
    def califica_estudiante(self, promedio):
        if 0 < promedio <= 55:
            return "REPROBADO"
        if promedio <= 65:
            return "CONVOCATORIA"
        if promedio <= 100:
            return "APROBADO"
        return None

    def append_promedio(self, row, promedio):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            line = lines[row]
            columns = line.split(",")
            COMPARA = 8
            if len(columns) < COMPARA:
                columns = columns[:6]+ [""]
            if len(columns) >= COMPARA:
                pass
            valor_promedio = "%2.0f" % promedio
            print(valor_promedio)
            columns = columns[0:7]+ [valor_promedio, "\n"]
            print(columns)
            lines[row] = ",".join(columns)
        with open(self.filename, 'w') as dbfile:
            dbfile.writelines(lines)

    def append_clasificacion(self, row, calificacion):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            line = lines[row]
            columns = line.split(",")
            columns = columns[:8]+ [calificacion] + columns[9:] + ["\n"]
            lines[row] = ",".join(columns)
        with open(self.filename, 'w') as dbfile:
            dbfile.writelines(lines)

    def count_rows(self):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            return len(lines)
        return -1

def clasifica_todos():
    db = Db('Excel_Bases.csv')
    row_quantity = db.count_rows()
    print(f"numero de rows {row_quantity}")
    for row in range(1, row_quantity):
        aplica = db.tiene_cantidad_notas_minimas(row)
        print(f"aplica? {aplica}")
        if not aplica:
            print("No tiene suficientes notas para ser calificado.")
            continue
        promedio = db.calcula_promedio(row)
        print(f"El promedio es: {promedio}")
        db.append_promedio(row, promedio)
        calificacion = db.califica_estudiante(promedio)
        if calificacion is None:
            print("Promedio invalido")
            continue
        db.append_clasificacion(row, calificacion)

db = Db('Excel_Bases.csv')

clasifica_todos() 
# print(db.tiene_cantidad_notas_minimas(2))