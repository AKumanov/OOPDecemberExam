from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def test_if_initializer_works_properly(self):
        t = Team('TeamName')
        self.assertEqual('TeamName', t.name)
        self.assertEqual({}, t.members)

    def test_incorrect_name_symbols_raises_message(self):
        expected = 'Team Name can contain only letters!'
        with self.assertRaises(ValueError) as vl:
            t = Team('#')
        self.assertEqual(expected, str(vl.exception))

    def test_add_member_method_appends_new_names_members(self):
        t = Team('Name')
        t.add_member(Peter=12, Alex=10)
        self.assertEqual(2, len(t.members))
        self.assertEqual({'Peter': 12, 'Alex': 10}, t.members)
        expected = 'Successfully added: Test, John'
        self.assertEqual(expected, t.add_member(Test=1, John=10))

    def test_remove_members_returns_message_if_member_not_found(self):
        t = Team('Name')
        t.add_member(John=10)
        expected = 'Member with name Alex does not exist'
        self.assertEqual(expected, t.remove_member('Alex'))
        self.assertEqual(1, len(t.members))

    def test_remove_member_removes_from_dict_and_returns_message(self):
        expected = 'Member Alex removed'
        t = Team('Name')
        t.add_member(Alex=10)
        self.assertEqual(expected, t.remove_member('Alex'))
        self.assertEqual({}, t.members)

    def test_greater_than_method_returns_true_if_len_is_bigger_else_false(self):
        t1 = Team('TeamOne')
        t2 = Team('TeamTwo')
        t1.add_member(Alex=10, Kevin=10, John=10)
        self.assertTrue(t1 > t2)
        self.assertEqual(True, t1 > t2)
        self.assertFalse(t2 > t1)

    def test_len_method_gets_the_correct_value(self):
        t1 = Team('TeamOne')
        t1.add_member(Alex=10, Kevin=10, John=10)
        expected = 3
        self.assertEqual(expected, len(t1))

    def test_add_method_creates_a_new_instance_with_combined_name_and_members(self):
        t1 = Team('TeamOne')
        t2 = Team('TeamTwo')
        t1.add_member(Alex=10, Tim=12)
        t2.add_member(John=15, Mark=30)
        test = t1 + t2
        self.assertEqual('TeamOneTeamTwo', test.name)
        self.assertEqual({'Alex': 10, 'Tim': 12, 'John': 15, 'Mark': 30}, test.members)

    def test_print_method(self):
        t1 = Team('TeamOne')
        t2 = Team('TeamTwo')
        t1.add_member(Alex=10)
        t2.add_member(John=15)
        test = t1 + t2
        expected = 'Team name: TeamOneTeamTwo\nMember: John - 15-years old\nMember: Alex - 10-years old'
        self.assertEqual(expected, str(test))


if __name__ == '__main__':
    main()
