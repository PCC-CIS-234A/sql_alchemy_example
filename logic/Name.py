# ============================================= Name.py ==========================================
# Logic layer

from data.Database import Database


class Name:
    __name = ""
    __year = 0
    __gender = ""
    __count = 0

    def __init__(self, name, gender, year, count):
        self.__year = year
        self.__name = name
        self.__gender = gender
        self.__count = count

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_year(self):
        return self.__year

    def get_count(self):
        return self.__count

    @staticmethod
    def read_names(name, gender):
        rows = Database.read_names(name, gender)
        return [Name(*row) for row in rows]

    def __repr__(self):
        return f"<Name {self.__name}, {self.__gender}, {self.__year}, {self.__count}>"

    def __str__(self):
        return f"<Name {self.__name}, {self.__gender}, {self.__year}, {self.__count}>"
