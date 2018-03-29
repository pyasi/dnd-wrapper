from .base import DnDBase
from .resource_dicts import *
from enum import Enum


class CharacterEnum(Enum):
    ability_score = 'ability-scores'
    skills = 'skills'
    proficiencies = 'proficiencies'
    languages = 'languages'


class Character(DnDBase):

    def __init__(self, resource):
        super(Character, self).__init__()
        self.resource = resource
        self.path = resource.value
        self.dict = self.get_dict_for_character_trait()

    def get_all(self):
        response = self._get(self.path)
        return response

    def info_by_id(self, resource_id):
        response = self._get(self.path + str(resource_id))
        return response

    def info_by_name(self, resource_name):
        resource_name = resource_name.lower()
        response = self.info_by_id(self.dict[resource_name])
        return response

    def get_dict_for_character_trait(self):

        if self.resource == CharacterEnum.ability_score:
            return ability_score_dict
        elif self.resource == CharacterEnum.skills:
            return skill_dict
        elif self.resource == CharacterEnum.proficiencies:
            return proficieny_dict
        elif self.resource == CharacterEnum.languages:
            return language_dict
