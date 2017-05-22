def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco
 
@deco
def myfunc():
    print("myfunc() called.")
    return 'ok'

a = myfunc()
