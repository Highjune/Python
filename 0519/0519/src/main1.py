#Python에서는 instance영역과 class영역이 분리된다.

class Test:
    name = '한지민'   #class variable


t = Test()
print(t.name)
print(Test.name)
t.name = '박지민'
print(t.name)
print(Test.name)
Test.name = '김지민'
print(t.name)
print(Test.name)
    