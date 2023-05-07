from .ConsoleMessageStyleInterface import ConsoleMessageStyleInterface
from cleo.commands.command import Command


class DefaultConsoleMessageStyle(ConsoleMessageStyleInterface):
    def __init__(self, command: Command):
        self.__command = command

    def success(self, message: str):
        self.__command.line(f'<fg=black;bg=green>[OK] {message}</>')

    def warning(self, message: str):
        self.__command.line(f'<fg=black;bg=yellow>[WARNING] {message}</>')

    def error(self, message: str):
        self.__command.line(f'<fg=white;bg=red>[ERROR] {message}</>')

    def info(self, message: str):
        self.__command.line(f'<fg=black;bg=blue>[INFO] {message}</>')
