# asgmt-6-programming-and-data-analysis-2023

> Assignment 6: Programming and Data Analysis 2023.

Define functions or classes in `asgmt-six.py` with given names and templates then run `test-runner.py`.

## 01. Define a class `SortArgs` which instantiates objects takes `*args` with two methods `sort_asc()` and `sort_desc()` that take flexible integers and return a sorted `list`.

```python
class SortArgs:
    """
    >>> sort_args = SortArgs()
    >>> type(sort_args)
    '__main__.SortArgs'
    >>> sort_args.sort_asc(1, 2, 0)
    [0, 1, 2]
    >>> sort_args.sort_desc(1, 2, 0)
    [2, 1, 0]
    >>> sort_args.sort_asc(4, 3, 5)
    [3, 4, 5]
    >>> sort_args.sort_desc(4, 3, 5)
    [5, 4, 3]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a class `FilterStrArgs()` which instantiates objects takes `*args` with 2 methods `get_str_args()` and `get_non_str_args()`.

```python
class FilterStrArgs:
    """
    >>> filter_str_args = FilterStrArgs("5566", 5566, False)
    >>> type(filter_str_args)
    '__main__.FilterStrArgs'
    >>> filter_str_args.get_str_args()
    ["5566"]
    >>> filter_str_args.get_non_str_args()
    [5566, False]
    >>> filter_str_args = FilterStrArgs("5566", 5566, False, True, "False", "True", "Luke Skywalker")
    >>> type(filter_str_args)
    '__main__.FilterStrArgs'
    >>> filter_str_args.get_str_args()
    ["5566", "False", "True", "Luke Skywalker"]
    >>> filter_str_args.get_non_str_args()
    [5566, False, True]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a class `ReduceArgs()` which instantiates objects takes `*args` with two methods `summation()` and `product()` that take flexible args and return aggregated result.

```python
class ReduceArgs:
    """
    >>> reduce_args = ReduceArgs(1, 2, 3, 4)
    >>> type(reduce_args)
    '__main__.ReduceArgs'
    >>> reduce_args.summation()
    10
    >>> reduce_args.product()
    24
    >>> reduce_args = ReduceArgs(1, 2, 3, 4, 5)
    >>> reduce_args.summation()
    15
    >>> reduce_args.product()
    120
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a class `ReverseKeyValues` which instantiates objects takes `**kwargs` with 2 attributes `keys` and `values`, 1 method `reverse()`.

```python
class ReverseKeyValues:
    """
    >>> reverse_key_values = ReverseKeyValues(twn='Taiwan')
    >>> type(reverse_key_values)
    '__main__.ReverseKeyValues'
    >>> reverse_key_values.keys
    ['twn']
    >>> reverse_key_values.values
    ['Taiwan']
    >>> reverse_key_values.reverse()
    {'Taiwan': 'twn'}
    >>> reverse_key_values = ReverseKeyValues(twn='Taiwan', jpn='Japan')
    >>> type(reverse_key_values)
    '__main__.ReverseKeyValues'
    >>> reverse_key_values.keys
    ['twn', 'jpn']
    >>> reverse_key_values.values
    ['Taiwan', 'Japan']
    >>> reverse_key_values.reverse()
    {'Taiwan': 'twn', 'Japan': 'jpn'}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a class `FizzBuzz` which instantiates objects with 2 methods `nth_element()` and `generate_sequence()`.

Source: <https://en.wikipedia.org/wiki/Fizz_buzz>

```python
class FizzBuzz:
    """
    >>> fizz_buzz = FizzBuzz()
    >>> type(fizz_buzz)
    '__main__.FizzBuzz'
    >>> fizz_buzz.nth_element(1)
    1
    >>> fizz_buzz.nth_element(3)
    'Fizz'
    >>> fizz_buzz.nth_element(5)
    'Buzz'
    >>> fizz_buzz.nth_element(15)
    'Fizz Buzz'
    >>> fizz_buzz.generate_sequence(5)
    [1, 2, 'Fizz', 4, 'Buzz']
    >>> fizz_buzz.generate_sequence(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `import_teams_json` which imports the `teams.json` as a `dict` in working directory.

```python
def import_teams_json() -> dict:
    """
    >>> teams_json = import_teams_json()
    >>> type(teams_json)
    dict
    >>> len(teams_json["data"])
    30
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `find_teams_conference_division` which returns a team's conference and division in a `tuple` given team's abbreviation, based on `teams.json` in working directory.

```python
def find_teams_conference_division(team_abb: str) -> tuple:
    """
    >>> find_teams_conference_division("BOS")
    ('East', 'Atlantic')
    >>> find_teams_conference_division("MIA")
    ('East', 'Southeast')
    >>> find_teams_conference_division("LAL")
    ('West', 'Pacific')
    >>> find_teams_conference_division("DEN")
    ('West', 'Northwest')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `find_teams_city` which returns a team's city given team's name, based on `teams.json` in working directory.

```python
def find_teams_city(team_name: str) -> str:
    """
    >>> find_teams_city("Celtics")
    'Boston'
    >>> find_teams_city("Heat")
    'Miami'
    >>> find_teams_city("Lakers")
    'Los Angeles'
    >>> find_teams_city("Nuggets")
    'Denver'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `summarize_pandemic_by_country()` which generates a DataFrame to summarize the pandemic globally as of 2023-03-09 given `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` in working directory.

PS. Time series data records the cumulative `Confirmed` and `Deaths` cases respectively.

```
           Country/Region  Confirmed  Deaths
0             Afghanistan     209451    7896
1                 Albania     334457    3598
2                 Algeria     271496    6881
3                 Andorra      47890     165
4                  Angola     105288    1933
..                    ...        ...     ...
196    West Bank and Gaza     703228    5708
197  Winter Olympics 2022        535       0
198                 Yemen      11945    2159
199                Zambia     343135    4057
200              Zimbabwe     264276    5671

[201 rows x 3 columns]
```

```python
def summarize_pandemic_by_country() -> pd.core.frame.DataFrame:
    """
    >>> pandemic_by_country = summarize_pandemic_by_country()
    >>> type(pandemic_by_country)
    pandas.core.frame.DataFrame
    >>> pandemic_by_country.shape
    (201, 3)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `find_taiwan_from_covid_time_series()` which generates a DataFrame of Taiwan's confirmed and deaths cases given `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` in working directory. Remove the asterisk in `Country/Region` column.

```
     Country/Region     Date  Confirmed  Deaths
0            Taiwan  1/22/20          1       0
1            Taiwan  1/23/20          1       0
2            Taiwan  1/24/20          3       0
3            Taiwan  1/25/20          3       0
4            Taiwan  1/26/20          4       0
...             ...      ...        ...     ...
1138         Taiwan   3/5/23    9970937   17672
1139         Taiwan   3/6/23    9970937   17672
1140         Taiwan   3/7/23    9970937   17672
1141         Taiwan   3/8/23    9970937   17672
1142         Taiwan   3/9/23    9970937   17672

[1143 rows x 4 columns]
```

```python
def find_taiwan_from_covid_time_series() -> pd.core.frame.DataFrame:
    """
    >>> taiwan_from_covid_time_series = find_taiwan_from_covid_time_series()
    >>> type(taiwan_from_covid_time_series)
    pandas.core.frame.DataFrame
    >>> taiwan_from_covid_time_series.shape
    (1143, 4)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```