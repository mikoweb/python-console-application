#!/usr/bin/env python

from cleo.application import Application
from dependency_injector.wiring import Provide, inject
from app.services.Container import Container

from app.module.sample.application.command.SampleHelloCommand import SampleHelloCommand
from app.module.sample.application.command.SampleMessagesCommand import SampleMessagesCommand
from app.module.sample.application.command.SampleProgressBarCommand import SampleProgressBarCommand
from app.module.sample.application.command.SampleTableCommand import SampleTableCommand


@inject
def main(
    sample_hello_command: SampleHelloCommand = Provide[Container.sample_hello_command],
    sample_messages_command: SampleMessagesCommand = Provide[Container.sample_messages_command],
    sample_progress_bar_command: SampleProgressBarCommand = Provide[Container.sample_progress_bar_command],
    sample_table_command: SampleTableCommand = Provide[Container.sample_table_command]
):
    application.add(sample_hello_command)
    application.add(sample_messages_command)
    application.add(sample_progress_bar_command)
    application.add(sample_table_command)
    application.run()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    application = Application()
    main()
