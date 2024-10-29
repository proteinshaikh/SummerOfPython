import threading
import random
from collections import defaultdict, Counter
from itertools import islice
from math import sqrt
from typing import List, Dict, Set


# Singleton Pattern with Double-Checked Locking
class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def do_something(self):
        print("Singleton action performed!")


# Find two indices in an array that add up to a target
def two_sum(arr: List[int], target: int) -> List[int]:
    lookup = {}
    for i, num in enumerate(arr):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []


# Count words in a sentence
def count_words(sentence: str) -> Dict[str, int]:
    words = sentence.split()
    return Counter(words)


# Calculate factorial using recursion
def factorial(num: int) -> int:
    return 1 if num <= 1 else num * factorial(num - 1)


# Rotate an array to the left
def rotate_array_left(arr: List[int], d: int) -> List[int]:
    return arr[d:] + arr[:d]


# Rotate an array to the right
def rotate_array_right(arr: List[int], d: int) -> List[int]:
    return arr[-d:] + arr[:-d]


# Reverse a string without using a temporary variable
def reverse_string_without_temp(s: str) -> str:
    return s[::-1]


# Find common elements between two arrays
def common_elements(arr1: List[int], arr2: List[int]) -> Set[int]:
    return set(arr1).intersection(arr2)


# Get the first non-repeated character in a string
def get_first_non_repeated_char(s: str) -> str:
    frequency = Counter(s)
    for char in s:
        if frequency[char] == 1:
            return char
    return ''


# Immutable and thread-safe class in Python
class ImmutablePerson:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


# Find the leader elements in an array
def find_leaders(arr: List[int]) -> List[int]:
    leaders = []
    max_right = float('-inf')
    for num in reversed(arr):
        if num > max_right:
            leaders.append(num)
            max_right = num
    return leaders[::-1]


# Find the most common element in an array
def most_common_element(arr: List[int]) -> int:
    return Counter(arr).most_common(1)[0][0]


# Remove duplicates from a list of integers
def remove_duplicates(lst: List[int]) -> List[int]:
    return list(set(lst))


# Remove duplicate words from a string
def remove_duplicate_words(sentence: str) -> str:
    words = sentence.split()
    return ' '.join(dict.fromkeys(words))


# Reverse the alphabets in a string
def reverse_alphabets(s: str) -> str:
    return ''.join(reversed(s))


# Find the second largest element in a list
def find_second_largest(lst: List[int]) -> int:
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None


# Count the occurrences of each alphabet in a string
def count_alphabets(s: str) -> Dict[str, int]:
    return Counter(s)


# Check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


# Find the maximum number in a list
def find_max_number(lst: List[int]) -> int:
    return max(lst)


# Create a thread using `Thread` class
class MyThread(threading.Thread):
    def run(self):
        print("Thread is running")


# Create a thread using `Runnable` interface
class MyRunnable:
    def run(self):
        print("Runnable is running")


# Lambda expression to print a greeting message
def lambda_greeting(name: str):
    greeting = lambda n: print(f"Hello, {n}")
    greeting(name)


# Join two lists
def join_lists(list1: List[int], list2: List[int]) -> List[int]:
    return list1 + list2


# Join two dictionaries (similar to maps)
def join_dicts(dict1: Dict, dict2: Dict) -> Dict:
    result = dict1.copy()
    for k, v in dict2.items():
        result[k] = result.get(k, '') + (', ' + v if k in result else v)
    return result


if __name__ == "__main__":
    # Test cases
    singleton = Singleton()
    singleton.do_something()

    print(two_sum([2, 7, 11, 15], 9))
    print(count_words("hello world hello"))
    print(factorial(5))
    print(rotate_array_left([1, 2, 3, 4, 5], 2))
    print(rotate_array_right([1, 2, 3, 4, 5], 2))
    print(reverse_string_without_temp("hello"))
    print(common_elements([1, 2, 3], [3, 4, 5]))
    print(get_first_non_repeated_char("swiss"))

    person = ImmutablePerson(1, "Zeeshan")
    print(person.name)

    print(find_leaders([16, 17, 4, 3, 5, 2]))
    print(most_common_element([1, 2, 3, 2, 4, 2, 5]))
    print(remove_duplicates([1, 2, 3, 3, 4, 5, 5]))
    print(remove_duplicate_words("hello world hello universe"))
    print(reverse_alphabets("abcdef"))
    print(find_second_largest([10, 20, 30, 40, 50]))
    print(count_alphabets("hello world"))
    print(is_palindrome("radar"))
    print(find_max_number([10, 20, 30, 40, 50]))

    # Threads
    thread1 = MyThread()
    thread1.start()

    runnable = MyRunnable()
    runnable_thread = threading.Thread(target=runnable.run)
    runnable_thread.start()

    lambda_greeting("Zeeshan")
    print(join_lists([1, 2, 3], [4, 5, 6]))
    print(join_dicts({'A': 'Apple', 'B': 'Banana'}, {'B': 'Blueberry', 'C': 'Cherry'}))
