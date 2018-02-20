#-*- coding:utf-8 -*- 

'''
        함수에 인자 전달하기

'''

def test1(arg1):
    print "arg1 :", arg1

test1('kim') 
# test1() 인자를 갯수만큼 전달하지 않으면 오류가난다.

def test2(a, b):
    print "a:", a, "b :", b

test2('dog', 'cat')
print "step06_function2.py 가 종료 됩니다." 
