class AppException(Exception):
    def __init__(self, message: str, code: int = 0, previous: Exception = None):
        self.__message = message
        self.__code = code
        self.__previous = previous

    @property
    def message(self) -> str:
        return self.__message

    @property
    def code(self) -> int:
        return self.__code

    @property
    def previous(self) -> Exception:
        return self.__previous
