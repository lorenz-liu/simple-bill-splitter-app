class Individual:
    def __init__(self, name, email=None, telephone=None, contribution=0) -> None:
        self.__name = name
        self.__email = email
        self.__telephone = telephone
        self.__contribution = contribution

    def __str__(self) -> str:
        return f"Individual {self.__name} ({self.__email}, {self.__telephone}) contributed {self.__contribution}"

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_telephone(self):
        return self.__telephone

    def get_contribution(self):
        return self.__contribution

    def add_contribution(self, amount):
        self.__contribution += amount
