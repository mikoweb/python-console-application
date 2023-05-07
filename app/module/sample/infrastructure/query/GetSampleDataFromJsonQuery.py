from app.module.core.domain.exception.FailedQueryException import FailedQueryException
from app.module.sample.domain.query.SampleDataQueryInterface import SampleDataQueryInterface
from app.module.sample.infrastructure.reader.SampleDataReader import SampleDataReader


class GetSampleDataFromJsonQuery(SampleDataQueryInterface):
    def get_data(self) -> list:
        """
        :raise app.module.core.domain.exception.FailedQueryException
        :rtype: list[app.module.sample.domain.dto.SampleDTO]
        """

        reader = SampleDataReader()
        try:
            return reader.read_from_json('storage/json/sample/sample_data_for_table.json')
        except Exception as exception:
            raise FailedQueryException('Get data failed', previous=exception)
