from app.module.core.application.path.app_path import app_path
import json

from app.module.sample.domain.dto.SampleDTO import SampleDTO


class SampleDataReader:
    def read_from_json(self, json_file_path: str) -> list:
        """
        :rtype: list[app.module.sample.domain.dto.SampleDTO]
        """

        json_file = open(app_path(json_file_path))
        json_data = json.load(json_file)

        sample_data = []
        for item in json_data:
            sample_data.append(self.map_item_to_dto(item))

        return sample_data

    def map_item_to_dto(self, item: dict) -> SampleDTO:
        return SampleDTO(first_name=item.get('firstName'), last_name=item.get('lastName'), age=item.get('age'))
