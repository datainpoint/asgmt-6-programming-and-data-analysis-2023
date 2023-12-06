import unittest
import importlib
import json
import numpy as np
import pandas as pd

class TestAssignmentSix(unittest.TestCase):
    def test_01_SortArgs(self):
        sort_args = asgmt.SortArgs()
        self.assertEqual(sort_args.sort_asc(1, 2, 0), [0, 1, 2])
        self.assertEqual(sort_args.sort_desc(1, 2, 0), [2, 1, 0])
        self.assertEqual(sort_args.sort_asc(4, 3, 5), [3, 4, 5])
        self.assertEqual(sort_args.sort_desc(4, 3, 5), [5, 4, 3])
    def test_02_FilterStrArgs(self):
        filter_str_args = asgmt.FilterStrArgs("5566", 5566, False)
        self.assertEqual(filter_str_args.get_str_args(), ["5566"])
        self.assertEqual(filter_str_args.get_non_str_args(), [5566, False])
        filter_str_args = asgmt.FilterStrArgs("5566", 5566, False, True, "False", "True", "Luke Skywalker")
        self.assertEqual(filter_str_args.get_str_args(), ["5566", "False", "True", "Luke Skywalker"])
        self.assertEqual(filter_str_args.get_non_str_args(), [5566, False, True])
    def test_03_ReduceArgs(self):
        reduce_args = asgmt.ReduceArgs(1, 2, 3)
        self.assertEqual(reduce_args.summation(), 6)
        self.assertEqual(reduce_args.product(), 6)
        reduce_args = asgmt.ReduceArgs(1, 2, 3, 4)
        self.assertEqual(reduce_args.summation(), 10)
        self.assertEqual(reduce_args.product(), 24)
        reduce_args = asgmt.ReduceArgs(1, 2, 3, 4, 5)
        self.assertEqual(reduce_args.summation(), 15)
        self.assertEqual(reduce_args.product(), 120)
    def test_04_ReverseKeyValues(self):
        reverse_key_values = asgmt.ReverseKeyValues(twn='Taiwan')
        self.assertEqual(reverse_key_values.keys, ['twn'])
        self.assertEqual(reverse_key_values.values, ['Taiwan'])
        self.assertEqual(reverse_key_values.reverse(), {'Taiwan': 'twn'})
        reverse_key_values = asgmt.ReverseKeyValues(twn='Taiwan', jpn='Japan')
        self.assertEqual(reverse_key_values.keys, ['twn', 'jpn'])
        self.assertEqual(reverse_key_values.values, ['Taiwan', 'Japan'])
        self.assertEqual(reverse_key_values.reverse(), {'Taiwan': 'twn', 'Japan': 'jpn'})
        reverse_key_values = asgmt.ReverseKeyValues(twn='Taiwan', jpn='Japan', usa='United States of America')
        self.assertEqual(reverse_key_values.keys, ['twn', 'jpn', 'usa'])
        self.assertEqual(reverse_key_values.values, ['Taiwan', 'Japan', 'United States of America'])
        self.assertEqual(reverse_key_values.reverse(), {'Taiwan': 'twn', 'Japan': 'jpn', 'United States of America': 'usa'})
    def test_05_FizzBuzz(self):
        fizz_buzz = asgmt.FizzBuzz()
        self.assertEqual(fizz_buzz.nth_element(1), 1)
        self.assertEqual(fizz_buzz.nth_element(3), 'Fizz')
        self.assertEqual(fizz_buzz.nth_element(5), 'Buzz')
        self.assertEqual(fizz_buzz.nth_element(15), 'Fizz Buzz')
        self.assertEqual(fizz_buzz.generate_sequence(5), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(fizz_buzz.generate_sequence(15), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])
    def test_06_import_teams_json(self):
        teams_json = asgmt.import_teams_json()
        self.assertIsInstance(teams_json, dict)
        self.assertEqual(len(teams_json["data"]), 30)
    def test_07_find_teams_conference_division(self):
        self.assertEqual(asgmt.find_teams_conference_division("BOS"), ('East', 'Atlantic'))
        self.assertEqual(asgmt.find_teams_conference_division("MIA"), ('East', 'Southeast'))
        self.assertEqual(asgmt.find_teams_conference_division("NYK"), ('East', 'Atlantic'))
        self.assertEqual(asgmt.find_teams_conference_division("PHI"), ('East', 'Atlantic'))
        self.assertEqual(asgmt.find_teams_conference_division("LAL"), ('West', 'Pacific'))
        self.assertEqual(asgmt.find_teams_conference_division("DEN"), ('West', 'Northwest'))
        self.assertEqual(asgmt.find_teams_conference_division("PHX"), ('West', 'Pacific'))
        self.assertEqual(asgmt.find_teams_conference_division("GSW"), ('West', 'Pacific'))
    def test_08_find_teams_city(self):
        self.assertEqual(asgmt.find_teams_city("Celtics"), "Boston")
        self.assertEqual(asgmt.find_teams_city("Heat"), "Miami")
        self.assertEqual(asgmt.find_teams_city("Knicks"), "New York")
        self.assertEqual(asgmt.find_teams_city("76ers"), "Philadelphia")
        self.assertEqual(asgmt.find_teams_city("Lakers"), "Los Angeles")
        self.assertEqual(asgmt.find_teams_city("Nuggets"), "Denver")
        self.assertEqual(asgmt.find_teams_city("Suns"), "Phoenix")
        self.assertEqual(asgmt.find_teams_city("Warriors"), "Golden State")
    def test_09_summarize_pandemic_by_country(self):
        pandemic_by_country = asgmt.summarize_pandemic_by_country()
        self.assertIsInstance(pandemic_by_country, pd.core.frame.DataFrame)
        self.assertEqual(pandemic_by_country.shape, (201, 3))
        self.assertEqual(pandemic_by_country["Country/Region"].nunique(), 201)
    def test_10_find_taiwan_from_covid_time_series(self):
        taiwan_from_covid_time_series = asgmt.find_taiwan_from_covid_time_series()
        self.assertIsInstance(taiwan_from_covid_time_series, pd.core.frame.DataFrame)
        self.assertEqual(taiwan_from_covid_time_series.shape, (1143, 4))
        self.assertEqual(taiwan_from_covid_time_series["Date"].nunique(), 1143)
        self.assertEqual(taiwan_from_covid_time_series["Country/Region"].nunique(), 1)

asgmt = importlib.import_module("asgmt-six")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentSix)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))