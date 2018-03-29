from pydnd import Race, Character, CharacterEnum, Class, ClassEnum, RaceEnum

import json

ab = Race(RaceEnum.subraces)
response = ab.get_all()
print("{")
for result in response['results']:
    print('"{}": {},'.format(result['name'].lower(), result['url'].split('/')[5]))
print("}")



# type = ab.info_by_name('common', as_object=True)
# print(type)
