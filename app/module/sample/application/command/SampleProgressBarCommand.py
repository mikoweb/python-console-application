from cleo.commands.command import Command
from cleo.helpers import argument
from progress.bar import Bar
import time
from app.module.core.application.console.ConsoleArgumentValidator import ConsoleArgumentValidator


class SampleProgressBarCommand(Command):
    DEFAULT_MAX_PROGRESS = 100
    DEFAULT_SLEEP_VALUE = 50

    name = 'sample:progress-bar'
    description = 'Sample command with Progress Bar'
    arguments = [
        argument('max_progress', description='Final value of progress', optional=True),
        argument('sleep', description='Command sleep value (ms)', optional=True),
    ]

    def __init__(self):
        super().__init__()
        self.__validator = ConsoleArgumentValidator(self)

    def handle(self) -> int:
        max_progress = int(self.argument('max_progress') or self.DEFAULT_MAX_PROGRESS)
        sleep = int(self.argument('sleep') or self.DEFAULT_SLEEP_VALUE)

        self.__validate_max_progress_value(max_progress)
        self.__validate_sleep_value(sleep)

        bar = Bar('Loading', max=max_progress)
        for i in range(max_progress):
            self.__sleep_command(sleep)
            bar.next()
        bar.finish()

        return 0

    def __sleep_command(self, sleep_ms: int):
        time.sleep(sleep_ms / 1000)

    def __validate_max_progress_value(self, max_progress: int):
        self.__validator.handle_validation('max_progress', max_progress, {'min': 1, 'max': 1000 * 1000 * 1000})

    def __validate_sleep_value(self, sleep: int):
        self.__validator.handle_validation('sleep', sleep, {'min': 1, 'max': 10000})
