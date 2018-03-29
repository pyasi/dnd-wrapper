from pydnd import Race, Character, CharacterEnum

import json

ab = Character(CharacterEnum.languages)
response = ab.get_all()
# print("{")
# for result in response['results']:
#     print('"{}": {},'.format(result['name'].lower(), result['url'].split('/')[5]))
# print("}")

type = ab.info_by_id(30, as_object=False)
print(type)
