class DataBase:
    def __init__(self, id, fullName, birthYear, exp, pos, department, note):
        self.id = id
        self.fullName = fullName
        self.birthYear = birthYear
        self.exp = exp
        self.pos = pos
        self.department = department
        self.note = note

    def showInfo(self):
        print(f'Табельный номер: {self.id}')
        print(f'ФИО : {self.fullName}')
        print(f'Год рождения : {self.birthYear}')
        print(f'Опыт : {self.exp}')
        print(f'Должность : {self.pos}')
        print(f'Кафедра : {self.department}')
        print(f'Примечание : {self.note}')

info = [
        DataBase(12 , "Исаев Валерий Алексеевич", 2006, 18, "Моушен дизайнер", "Кафедра Информатики", "Хочется писать на QT в C++"),
        DataBase(13 , "Нормис Безопснич Линуксоидович", 988, 20, "Кибер Безопасность", "Кафедра Информатики", "Стаж 100 лет, до сих пор не нашел работу"),
        DataBase(14 , "НеНормис Безопснич Линуксоидович", 228, 20, "Кибер Безопасность", "Кафедра Информатики", "Стаж 500 лет, до сих пор не нашел работу"),
        DataBase(15 , "РедФлагич Безопснич Линуксоидович", 161, 20, "Кибер Безопасность", "Кафедра Информатики", "Стаж 3 года, работает в Касперском, пишет код с 5 лет"),
        DataBase(16 , "ГринФлагич Безопснич Линуксоидович", 195, 20, "Кибер Безопасность", "Кафедра Информатики", "Стаж 100 лет, до сих пор не нашел работу"),
    ]

def displayExp20(info):
    print("Сотрудники со стажем 20 лет: ")
    for emp in info:
        if emp.exp == 20:
            emp.showInfo()

def displayPos(info):
    print("Сотрудники с должностью '{pos}' : ")
    for emp in info:
        emp.showInfo()


displayExp20(info)

posToFind = input("Введите доложность : ")
displayPos(info, posToFind)



