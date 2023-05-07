from cleo.commands.command import Command

from app.module.core.application.style.console.DefaultConsoleMessageStyle import DefaultConsoleMessageStyle
from app.module.core.domain.exception.FailedQueryException import FailedQueryException
from app.module.sample.infrastructure.query.GetSampleDataFromJsonQuery import GetSampleDataFromJsonQuery
from prettytable import PrettyTable


class SampleTableCommand(Command):
    name = 'sample:table'
    description = 'Sample command with Table'

    def __init__(self, query: GetSampleDataFromJsonQuery):
        super().__init__()
        self.__query = query

    def handle(self) -> int:
        try:
            sample_data = self.__query.get_data()
        except FailedQueryException:
            return self.__catch_cannot_load_sample_data()

        table = PrettyTable()
        table.field_names = ['First Name', 'Last Name', 'Age']

        for item in sample_data:
            table.add_row([item.first_name, item.last_name, item.age])

        print(table)

        return 0

    def __catch_cannot_load_sample_data(self) -> int:
        message_style = DefaultConsoleMessageStyle(self)
        message_style.error('Cannot load sample data!')

        return 1
