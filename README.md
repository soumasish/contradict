Contra[dict]
======================


## Description
Contradict provides a thread-safe implementation of the SortedDict. A SortedDict is a dict which can be traversed in ascending or descending order. This is different from the OrderedDict which can be traversed in the order in which the elements were added. The collection type exposes APIs to perform the following operations```get```, ```set```, ```contains```, ```items```, ```keys``` and ```value```.

#### Object Usage
For adding an object to the SortedDict, the object needs to implement it's comparator logic and a hash function.
```
class GitRepo:
    def __init__(self, url, stars, forks):
        self.url = url
        self.stars = stars
        self.forks = forks
    
    # The object needs to implement the following methods
    def __eq__(self, other):
        return self.name == other.name and self.stars == other.stars and self.forks == other.forks

    def __ne__(self, other):
        return self.name != other.name or self.stars != other.stars or self.forks != other.forks
    
    def __lt__(self, other):
        # The two repos are first compared based on stars then forks and then sorted lexically based on url
        if self.stars == other.stars and self.forks == other.forks return self.url < other.url

    def __le__(self, other):
        if self.stars == other.stars and self.forks == other.forks return self.url <= other.url

    def __gt__(self, other):
        if self.stars == other.stars and self.forks == other.forks return self.url > other.url

    def __ge__(self, other):
        if self.stars == other.stars and self.forks == other.forks return self.url >= other.url
    # Use any unique attribute to hash
    def __hash__(self):
        return hash(self.url)


```

## Dependencies
Python 3

## Installation
```
pip install --upgrade contradict
```

## Usage

```
from contradict.sorted_dict import SortedDict


sorted_dict = SortedDict()           # Creates an empty MaxHeap
sorted_dict.set(key, value)          # Sets a key, value pair
sorted_dict.get(key)                 # Returns the value, if key is present or None
sorted_dict.items()                  # Returns an interator to the key, value pairs in asc order
sorted_dict.keys()                   # Returns an interator to the keys in asc order
sorted_dict.values()                 # Returns an interator to the values in asc order of keys
sorted_dict.items(reverse=True)      # Returns an interator to the key, value pairs in desc order
sorted_dict.keys(reverse=True)       # Returns an interator to the keys in desc order
sorted_dict.values(reverse=True)     # Returns an interator to the values in desc order of keys

```

## License
MIT

## Changelog
##### 2.0.0
- Added thread safety and fixed a bug with reverse sorting
##### 1.0.2
- Updated README


