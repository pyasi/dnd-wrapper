from pydnd import Race, AbilityScore, Skill, Proficiency, Languages, Character, Resource

import json

ab = Resource(Character.languages)
response = ab.get_all()
print("{")
for result in response['results']:
    print('"{}": {},'.format(result['name'].lower(), result['url'].split('/')[5]))
print("}")

#print(ab.info_by_name('Flute'))