import abc


class Hashmap(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

    @abc.abstractmethod
    def contains(self, key):
        pass

    @abc.abstractmethod
    def items(self, reverse=False):
        pass

    @abc.abstractmethod
    def keys(self, reverse=False):
        pass

    @abc.abstractmethod
    def values(self, reverse=False):
        pass
