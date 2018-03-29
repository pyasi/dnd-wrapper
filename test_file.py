from pydnd import Race, Character, CharacterEnum, Classes, ClassesEnum

import json

ab = Classes(ClassesEnum.starting_equipment)
response = ab.get_all()
print("{")
for result in response['results']:
    print('"{}": {},'.format(result['name'].lower(), result['url'].split('/')[5]))
print("}")

# type = ab.info_by_name('common', as_object=True)
# print(type)
