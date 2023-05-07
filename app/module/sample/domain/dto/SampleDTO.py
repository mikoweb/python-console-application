class SampleDTO:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def age(self) -> int:
        return self.__age
