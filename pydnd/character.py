from .base import DnDBase
from .resource_dicts import *
from enum import Enum
import logging


class CharacterEnum(Enum):
    ability_score = 'ability-scores/'
    skills = 'skills/'
    proficiencies = 'proficiencies/'
    languages = 'languages/'


class Character(DnDBase):

    def __init__(self, resource):
        super(Character, self).__init__()
        self.resource = resource
        self.path = resource.value
        self.dict = self.get_dict_for_character_trait()

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

        if self.resource == CharacterEnum.ability_score:
            return ability_score_dict
        elif self.resource == CharacterEnum.skills:
            return skill_dict
        elif self.resource == CharacterEnum.proficiencies:
            return proficieny_dict
        elif self.resource == CharacterEnum.languages:
            return language_dict
