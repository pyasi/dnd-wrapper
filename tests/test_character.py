from pydnd import Character, CharacterEnum
import unittest


class CharacterLanguageTests(unittest.TestCase):

    from pydnd.resource_dicts import language_dict

    def setUp(self):
        self.languages = Character(CharacterEnum.languages)

    def test_languages_info_by_id_json(self):
        response = self.languages.info_by_id(1)
        self.assertIsInstance(response, dict)

    def test_languages_info_by_id_object(self):
        response = self.languages.info_by_id(1, as_object=True)
        self.assertEqual(response.type, 'Standard')
        self.assertIsInstance(response, object)

    def test_languages_info_by_name_json(self):
        response = self.languages.info_by_name('Common')
        self.assertIsInstance(response, dict)

    def test_languages_info_by_name_object(self):
        response = self.languages.info_by_name('Common', as_object=True)
        self.assertEqual(response.type, 'Standard')
        self.assertIsInstance(response, object)

    def test_can_make_multiple_objects(self):
        response_one = self.languages.info_by_name('Common', as_object=True)
        response_two = Character(CharacterEnum.languages).info_by_name('Elvish', as_object=True)
        self.assertNotEqual(response_one.index, response_two.index)

    def test_languages_get_all(self):
        response = self.languages.get_all()
        self.assertIsInstance(response, dict)

    def test_get_dict_for_trait(self):
        dictionary = self.languages.get_dict_for_character_trait()
        self.assertEqual(dictionary, self.language_dict)

    def test_language_id_negative_case(self):
        response = self.languages.info_by_id(30)
        self.assertIsNone(response)

    def test_language_name_negative_case_using_id(self):
        response = self.languages.info_by_name('NOT_LANGUAGE')
        self.assertIsNone(response)

    def test_language_name_negative_case_using_id(self):
        response = self.languages.info_by_name(300)
        self.assertIsNone(response)

class CharacterSkillsTests(unittest.TestCase):

    from pydnd.resource_dicts import skill_dict

    def setUp(self):
        self.skills = Character(CharacterEnum.skills)

    def test_skills_info_by_id_json(self):
        response = self.skills.info_by_id(1)
        self.assertIsInstance(response, dict)

    def test_skills_info_by_id_object(self):
        response = self.skills.info_by_id(1, as_object=True)
        self.assertEqual(response.name, 'Acrobatics')
        self.assertIsInstance(response, object)

    def test_skills_info_by_name_json(self):
        response = self.skills.info_by_name('Acrobatics')
        self.assertIsInstance(response, dict)

    def test_skills_info_by_name_object(self):
        response = self.skills.info_by_name('Acrobatics', as_object=True)
        self.assertEqual(response.name, 'Acrobatics')
        self.assertIsInstance(response, object)

    def test_can_make_multiple_objects(self):
        response_one = self.skills.info_by_name('Acrobatics', as_object=True)
        response_two = Character(CharacterEnum.skills).info_by_name('Arcana', as_object=True)
        self.assertNotEqual(response_one.index, response_two.index)

    def test_skills_get_all(self):
        response = self.skills.get_all()
        self.assertIsInstance(response, dict)

    def test_get_dict_for_trait(self):
        dictionary = self.skills.get_dict_for_character_trait()
        self.assertEqual(dictionary, self.skill_dict)

    def test_skills_id_negative_case(self):
        response = self.skills.info_by_id(300)
        self.assertIsNone(response)

    def test_skills_name_negative_case_using_id(self):
        response = self.skills.info_by_name('NOT_SKILL')
        self.assertIsNone(response)

    def test_skills_name_negative_case_using_id(self):
        response = self.skills.info_by_name(300)
        self.assertIsNone(response)


class CharacterProficienciesTests(unittest.TestCase):

    from pydnd.resource_dicts import proficieny_dict

    def setUp(self):
        self.proficiencies = Character(CharacterEnum.proficiencies)

    def test_skills_info_by_id_json(self):
        response = self.proficiencies.info_by_id(1)
        self.assertIsInstance(response, dict)

    def test_skills_info_by_id_object(self):
        response = self.proficiencies.info_by_id(1, as_object=True)
        self.assertEqual(response.name, 'Light armor')
        self.assertIsInstance(response, object)

    def test_skills_info_by_name_json(self):
        response = self.proficiencies.info_by_name('Light armor')
        self.assertIsInstance(response, dict)

    def test_skills_info_by_name_object(self):
        response = self.proficiencies.info_by_name('Light armor', as_object=True)
        self.assertEqual(response.type, 'Armor')
        self.assertIsInstance(response, object)

    def test_can_make_multiple_objects(self):
        response_one = self.proficiencies.info_by_name('Light armor', as_object=True)
        response_two = Character(CharacterEnum.proficiencies).info_by_name('Medium armor', as_object=True)
        self.assertNotEqual(response_one.index, response_two.index)

    def test_skills_get_all(self):
        response = self.proficiencies.get_all()
        self.assertIsInstance(response, dict)

    def test_get_dict_for_trait(self):
        dictionary = self.proficiencies.get_dict_for_character_trait()
        self.assertEqual(dictionary, self.proficieny_dict)

    def test_skills_id_negative_case(self):
        response = self.proficiencies.info_by_id(300)
        self.assertIsNone(response)

    def test_skills_name_negative_case_using_id(self):
        response = self.proficiencies.info_by_name('NOT_PROFICIENCY')
        self.assertIsNone(response)

    def test_skills_name_negative_case_using_id(self):
        response = self.proficiencies.info_by_name(300)
        self.assertIsNone(response)
