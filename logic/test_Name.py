import unittest
from unittest.mock import patch
from Name import Name


class TestName(unittest.TestCase):

    # tests the constructor and getters
    def test_name_instance_values(self):
        # Actual
        n = Name('Anna', 'F', 1995, 85)

        # Assert
        self.assertEqual(n.get_name(), 'Anna')
        self.assertEqual(n.get_gender(), 'F')
        self.assertEqual(n.get_year(), 1995)
        self.assertEqual(n.get_count(), 85)

    # This tests whether the conversion from database results to Name objects is correct.
    @patch('Name.Database.read_names')
    def test_read_names_returns_expected_objects(self, mock_read_names):
        NAME = 'Marc'
        GENDER = 'M'

        # Mock DB results
        mock_read_names.return_value = [
            (NAME, GENDER, 2000, 100),
            (NAME, GENDER, 2001, 120),
        ]

        # Act
        result = Name.read_names(NAME, GENDER)

        # Assert
        self.assertEqual(len(result), 2)

        self.assertEqual(result[0].get_name(), NAME)
        self.assertEqual(result[0].get_gender(), GENDER)
        self.assertEqual(result[0].get_year(), 2000)
        self.assertEqual(result[0].get_count(), 100)

        self.assertEqual(result[0].get_name(), result[1].get_name())
        self.assertEqual(result[0].get_gender(), result[1].get_gender())
        self.assertEqual(result[1].get_year(), 2001)
        self.assertEqual(result[1].get_count(), 120)

    # Since the above checks whether the conversion to Name objects works properly,
    # this part will fail if the database in returning incorrect results.
    def test_read_names_actual_data(self):
        name = 'Marc'
        gender = 'M'
        # Act
        result = Name.read_names(name, gender)

        # Assert
        self.assertEqual(len(result), 100)

        # Just going to check the length and the first couple of values.
        self.assertEqual(result[0].get_name(), name)
        self.assertEqual(result[0].get_gender(), gender)
        self.assertEqual(result[0].get_year(), 1915)
        self.assertEqual(result[0].get_count(), 13)

        self.assertEqual(result[1].get_count(), 14)
        self.assertEqual(result[1].get_year(), 1916)

        self.assertEqual(result[2].get_count(), 9)
        self.assertEqual(result[2].get_year(), 1917)

    # Testing when an unknown name is used
    def test_read_names_unknown_name(self):
        name = "Not a real name"
        gender = "F"
        results = Name.read_names(name, gender)
        self.assertEqual(len(results), 0)

    # Testing when an unknown gender is used
    def test_read_names_unknown_gender(self):
        name = "Jane"
        gender = "X"
        results = Name.read_names(name, gender)
        self.assertEqual(len(results), 0)

    # Make sure we raise an exception if read_names is called with the wrong number of arguments
    def test_wrong_number_of_arguments(self):
        name = "X"
        with self.assertRaises(TypeError):
            Name.read_names(name)


if __name__ == '__main__':
    unittest.main()
