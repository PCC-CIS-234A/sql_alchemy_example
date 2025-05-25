# ================================== NamesUI.py =====================================
# Presentation layer

from logic.Name import Name


class NamesUI:
    @staticmethod
    def input_name():
        while True:
            name = input("Please enter a name or Q for quit: ")
            if name != "":
                return name
            print("Name must be non-empty.")

    @staticmethod
    def input_gender():
        while True:
            gender = input("Please enter a gender (M/F): ").upper()
            if gender in ["M", "MALE"]:
                return "M"
            if gender in ["F", "FEMALE"]:
                return "F"
            print("Gender must be M or F.")

    @staticmethod
    def display(names):
        print(f"{'Name':20} {'Gender':^8} {'Year':^6} {'Count':^7}")
        print(f"{'='*20} {'='*8} {'='*6} {'='*7}")
        for name in names:
            print(f"{name.get_name():20} {name.get_gender():^8} {name.get_year():^6} {name.get_count():^7}")

    @classmethod
    def run(cls):
        while True:
            name = cls.input_name()
            if name == "Q" or name == "q":
                print("Thanks for using the Names App!")
                return
            gender = cls.input_gender()

            names = Name.read_names(name, gender)

            print()
            cls.display(names)
            print()


if __name__ == "__main__":
    NamesUI.run()