from .base import DnDBase
from .resource_dicts import *
from enum import Enum
import logging


class ClassesEnum(Enum):
    classes = 'classes/'
    subclasses = 'subclasses/'
    #features = 'features/'
    #spellcasting = 'spellcasting/'
    #starting_equipment = 'startingequipment/'


class Classes(DnDBase):

    def __init__(self, resource):
        super(Classes, self).__init__()
        self.resource = resource
        self.path = resource.value
        #self.dict = self.get_dict_for_character_trait()

    def get_all(self):
        response = self._get(self.path)
        return response

    def info_by_id(self, resource_id, as_object=False):
        response = self._get(self.path + str(resource_id))
        self._set_response_info_to_class_values(response)
        if as_object:
            self._set_response_info_to_class_values(response)
            return self
        return response

    def info_by_name(self, resource_name, as_object=False):
        if not isinstance(resource_name, str):
            return None
        resource_name = resource_name.lower()
        try:
            response = self.info_by_id(self.dict[resource_name], as_object=as_object)
            return response
        except KeyError as e:
            logging.error('Value "{}" not available as a resource- Error: {}'.format(resource_name, e))
            return None

    def get_dict_for_character_trait(self):

        if self.resource == ClassesEnum.classes:
            return classes_dict
        elif self.resource == ClassesEnum.subclasses:
            return subclasses_dict

