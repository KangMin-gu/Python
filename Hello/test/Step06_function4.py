#-*- coding:utf-8 -*- 
'''
     함수에 인자를 원하는 곳에 전달하기
'''

def test1(num, name, addr):
    
    print "num : ", num, "name : ", name, "addr : ", addr
    
test1(1, "김구라", "노량진")
#keyword 인자 전달 (순서대로 정렬하지 않아도 알아서 찾아간다.)
test1(name="해골", addr="행신동", num=2)

print "---------------------------------------------------------"

# 함수를 선언할때 전달되는 인자의 default(기본) 값을 지정할 수 있다. 

def test2(num=0, name="아무게", addr="어디게"):
    print "num : ", num, "name : ", name, "addr :", addr

test2()
test2(num=999)
test2(num=999, name="원숭이")
test2(num=999, name="원숭이", addr="행신동")


















