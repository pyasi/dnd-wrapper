from .base import DnDBase
from .resource_dicts import *
from enum import Enum


class ClassesEnum(Enum):
    classes = 'classes'
    subclasses = 'subclasses'
    features = 'features'
    spellcasting = 'spellcasting'
    starting_equipment = 'starting-equipment'

