from .base import DnDBase
import logging


class Race(DnDBase):

    def __init__(self):
        super(Race, self).__init__()
        self.path = 'races/'

    def get_all(self):
        response = self._get(self.path)
        return response

    def info_by_id(self, race_id):
        response = self._get(self.path + str(race_id))
        return response

    def info_by_name(self, race_name):
        race_name = race_name.lower()
        try:
            response = self.info_by_id(self.race_dict[race_name])
            return response
        except KeyError as e:
            logging.error('Must use of of: {}'.format(self.race_dict))
            raise e
