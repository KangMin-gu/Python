#-*- coding:utf-8 -*- 
'''
    함수에 여러개의 인자를 동적으로 전달하기

'''

def test1(*args):
    # *를 붙여놓으면 args 는 tuple type 이다. tuple 타입으로 전달됨. 
    print args
    
test1()
test1(10)
test1(10, 20)    
test1(10, 20, 30)
test1('one', 'two', True)
#인자를 한개 해도되고 2개해도되고 3개해도되고 동적으로 전달 가능하다.
print "Step06_function3.py 가 종료 됩니다."    