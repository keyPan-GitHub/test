# 我们去检查某个类是否某种方法。


class Company(object):

    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __len__(self):
        return len(self.employee_list)


com = Company(["bobby1", "bobby2"])
print(hasattr(com, "__len__"))
# print(len(com))

#我们在某些情况下，希望判定某个对象的类型
from collections.abc import Sized
isinstance(com, Sized)

#我们需要强制某个子类，必须实现某写方法
#实现了一个Web框架，集成cache（redis，cache，memorycache）
#需要设计一个抽象基类，指定子类必须实现某些方法。

import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key, value):
        pass
    
    @abc.abstractmethod
    def set(self, key):
        pass
# class CacheBase():

#     def get(self, key, value):
#         raise NotImplementedError

#     def set(self, key):
#         raise NotImplementedError


class RedisCache(CacheBase):

    def set(self, key, value):
        pass

    def get(self, key, value):
        pass

redis_cache = RedisCache()
# redis_cache.set("key", "Value")
