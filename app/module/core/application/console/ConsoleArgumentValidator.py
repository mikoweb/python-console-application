from cleo.commands.command import Command
from cerberus import Validator
from app.module.core.application.style.console.DefaultConsoleMessageStyle import DefaultConsoleMessageStyle


class ConsoleArgumentValidator:
    def __init__(self, command: Command):
        self.__command = command
        self.__message_style = DefaultConsoleMessageStyle(self.__command)
        self.__last_validator = None

    def handle_validation(self, argument_name: str, value, rules: dict):
        is_valid = self.validate(argument_name, value, rules)

        if not is_valid:
            error = self.__get_error(argument_name)
            self.__message_style.error(f'Invalid argument {argument_name}: {error}')
            exit(1)

    def validate(self, argument_name: str, value, rules: dict) -> bool:
        validator = Validator({argument_name: rules})
        self.__last_validator = validator
        is_valid = validator.validate({argument_name: value})

        return is_valid

    def __get_error(self, argument_name: str) -> str:
        return self.__last_validator.errors[argument_name][0]
