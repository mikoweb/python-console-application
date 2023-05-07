from abc import ABC, abstractmethod


class ConsoleMessageStyleInterface(ABC):
    @abstractmethod
    def success(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def warning(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def error(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def info(self, message: str):
        raise NotImplementedError
