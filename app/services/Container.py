from dependency_injector import containers, providers

from app.module.sample.application.command.SampleHelloCommand import SampleHelloCommand
from app.module.sample.application.command.SampleMessagesCommand import SampleMessagesCommand
from app.module.sample.application.command.SampleProgressBarCommand import SampleProgressBarCommand
from app.module.sample.application.command.SampleTableCommand import SampleTableCommand
from app.module.sample.infrastructure.query.GetSampleDataFromJsonQuery import GetSampleDataFromJsonQuery


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    sample_hello_command = providers.Singleton(SampleHelloCommand)
    sample_messages_command = providers.Singleton(SampleMessagesCommand)
    sample_progress_bar_command = providers.Singleton(SampleProgressBarCommand)

    sample_table_command = providers.Singleton(
        SampleTableCommand,
        query=providers.Singleton(GetSampleDataFromJsonQuery)
    )

