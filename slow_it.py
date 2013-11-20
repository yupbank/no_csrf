import time

def slow(d=1):
    def _(fn):
        def __(*args, **kwargs):
            time.sleep(d)
            return fn(*args, **kwargs)
        return __
    return _
            

@slow()
def test(a):
    print a

def main():
    for i in xrange(10):
        test(i)

if __name__ == "__main__":
    main()
