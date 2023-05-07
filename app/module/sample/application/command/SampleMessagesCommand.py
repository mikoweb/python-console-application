from cleo.commands.command import Command
from app.module.core.application.style.console.DefaultConsoleMessageStyle import DefaultConsoleMessageStyle


class SampleMessagesCommand(Command):
    name = 'sample:messages'
    description = 'Display messages e.g. warning, error, information'

    def handle(self) -> int:
        message_style = DefaultConsoleMessageStyle(self)
        message_style.success('Success')
        message_style.warning('Warning!')
        message_style.error('Error!')
        message_style.info('Info')

        return 0
