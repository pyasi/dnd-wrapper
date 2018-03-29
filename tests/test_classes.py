from pydnd import Class, ClassEnum
import unittest


class ClassesTests(unittest.TestCase):

    from pydnd.resource_dicts import classes_dict

    def setUp(self):
        self.classes = Class(ClassEnum.classes)

    def test_class_info_by_id_json(self):
        response = self.classes.info_by_id(1)
        self.assertIsInstance(response, dict)

    def test_class_info_by_id_object(self):
        response = self.classes.info_by_id(1, as_object=True)
        self.assertEqual(response.name, 'Barbarian')
        self.assertIsInstance(response, object)

    def test_class_info_by_name_json(self):
        response = self.classes.info_by_name('Barbarian')
        self.assertIsInstance(response, dict)

    def test_class_info_by_name_object(self):
        response = self.classes.info_by_name('Barbarian', as_object=True)
        self.assertEqual(response.hit_die, 12)
        self.assertIsInstance(response, object)

    def test_can_make_multiple_objects(self):
        response_one = self.classes.info_by_name('Barbarian', as_object=True)
        response_two = Class(ClassEnum.classes).info_by_name('Bard', as_object=True)
        self.assertNotEqual(response_one.index, response_two.index)

    def test_class_get_all(self):
        response = self.classes.get_all()
        self.assertIsInstance(response, dict)

    def test_get_dict_for_trait(self):
        dictionary = self.classes.get_dict_for_character_trait()
        self.assertEqual(dictionary, self.classes_dict)

    def test_class_id_negative_case(self):
        response = self.classes.info_by_id(300)
        self.assertIsNone(response)

    def test_class_name_negative_case_using_id(self):
        response = self.classes.info_by_name('NOT_CLASS')
        self.assertIsNone(response)

    def test_class_name_negative_case_using_id(self):
        response = self.classes.info_by_name(300)
        self.assertIsNone(response)