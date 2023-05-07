from abc import ABC, abstractmethod


class SampleDataQueryInterface(ABC):
    @abstractmethod
    def get_data(self) -> list:
        """
        :raise app.module.core.domain.exception.FailedQueryException
        :rtype: list[app.module.sample.domain.dto.SampleDTO]
        """
        raise NotImplementedError
