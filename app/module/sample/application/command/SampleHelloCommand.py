from cleo.commands.command import Command
from cleo.helpers import option
from app.module.core.application.console.ConsoleArgumentValidator import ConsoleArgumentValidator


class SampleHelloCommand(Command):
    name = 'sample:hello'
    description = 'Hello message'
    options = [
        option('name', flag=False, description='Your Name', default='World')
    ]

    def __init__(self):
        super().__init__()
        self.__validator = ConsoleArgumentValidator(self)

    def handle(self) -> int:
        name = self.option('name')
        self.__validate_name_value(name)

        self.line(f'Hello {name}')

        return 0

    def __validate_name_value(self, max_progress: int):
        self.__validator.handle_validation('max_progress', max_progress, {'minlength': 1, 'maxlength': 255})
