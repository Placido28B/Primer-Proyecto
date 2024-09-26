
class Utils():

    @staticmethod
    def ask_id():
        id_correct = False
        while not id_correct:
            try:
                user_id = int(input("Write the student ID: \n"))
            except ValueError:
                print("Only numbers are allowed.")
                continue

            if user_id > 999999999:
                print("Wrong, you have extra numbers.")
                continue

            if user_id < 100000000:
                print("Wrong, you are missing numbers.")
                continue
            id_correct = True
        return str(user_id)

    @staticmethod
    def ask_grade():
        grade_correct = False
        while not grade_correct:
            try:
                grade = int(input("Write the note: \n"))
            except ValueError:
                print("Only numbers are allowed.")
                continue

            if not (0<=grade<=100):
                print("Wrong, the note only goes from 0 to 100.")
                continue

            grade_correct = True
        return grade

class Db():

    def __init__(self, filename):
        self.filename = filename
    
    def find_id_in_db(self, identification_card):
        with open(self.filename, 'r') as dbfile:
            row = 0
            lines = dbfile.readlines()
            for line in lines:
                columns = line.split(',')
                if identification_card==columns[0]:
                    return row
                row += 1
            return False
            row = -1
            return row

    def append_grade(self, row, grade):
        with open(self.filename, 'r') as dbfile:
            lines = dbfile.readlines()
            if row >=len(lines) or row<1:
                print(f"Invalid Row {row}, nothing done")
                return
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades)>=5:
                print("No more grades allowed")
                return
            print("Grade Save")
            columns = columns[:-1]+ [str(grade), "\n"]
            lines[row] = ",".join(columns)
        with open(self.filename, 'w') as dbfile:
            dbfile.writelines(lines)

    def allows_more_grades(self, row):
        with open(self.filename, 'r') as verifica:
            lines = verifica.readlines()
            line = lines[row]
            columns = line.split(',')
            grades = columns[3:]
            if len(grades)>=5:
                return False
            return True

def insert_grade():
    row = -1
    db = Db('Excel_Bases.csv')
    while row < 1:
        identification_card = Utils.ask_id()
        row = db.find_id_in_db(identification_card)
        if db.find_id_in_db(identification_card) is False:
            print(f'The id {identification_card} was not found')
            continue
        print("Correct ID")
        pass
        db.allows_more_grades(row)
        if db.allows_more_grades(row) is False:
            print("No more grades"[::1])
            break
        elif db.allows_more_grades(row) is True:
            pass
        nota = Utils.ask_grade() 
        db.append_grade(row, nota)
        break          
insert_grade()