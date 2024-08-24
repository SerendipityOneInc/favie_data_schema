import re
import hashlib

class CommonUtils():
    @staticmethod
    def all_not_none(*args):
        return all([arg is not None for arg in args])
    
    @staticmethod
    def any_none(*args):
        return any([arg is None for arg in args])
    
    @staticmethod
    def all_none(*args):
        return all([arg is None for arg in args])    
    
    @staticmethod
    def any_not_none(*args):
        return any([arg is not None for arg in args])
    
    @staticmethod
    def host_trip_www(host:str):
        return re.sub(r'^www\.', '', host) if host is not None else None
    
    @staticmethod
    def md5_hash(text:str):
        return hashlib.md5(text.encode()).hexdigest()
    
    @staticmethod
    def list_len(list):
        return len(list) if list is not None else 0
    
    @staticmethod
    def divide_chunks(lst, n):
        # 计算每个分片应有的长度
        chunk_size = len(lst) // n + (1 if len(lst) % n > 0 else 0)
        # 生成分片
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

if __name__ == "__main__":
    print(CommonUtils.all_not_none(1, 2, 3))
    print(CommonUtils.all_not_none(1, 2, None))
    print(CommonUtils.any_none(1, 2, 3))
    print(CommonUtils.any_none(1, 2, None))
    print(CommonUtils.all_none(None, None, None))
    print(CommonUtils.all_none(None, None, 1))
    print(CommonUtils.md5_hash("hello"))
    print(CommonUtils.divide_chunks([1,2,3,4,5,6],4))


