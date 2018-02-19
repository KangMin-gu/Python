#-*- coding:utf-8 -*- 


# int type (정수)
num1 = 10

# float type (실수)
num2 = 10.1

# bool type (논리)
isRun = True
isWait = False
isGreater = 10>5

# str type (문자)
myName = 'kimgura'
youName = "monkey"

# unicode type (한글을 다룰때는 uicode type (u) 를 앞에 써야한다.)
ourName = u'에이콘'
ourName2 = u"에이콘 아카데미"

# list type
nums = [10,20,30,40,50] #int type 을 저장하고 있는 list
names = ['kim', 'lee', 'park'] # str type 을 저장하고 있는 list
friends = [u'김구라', u'해골', u'원숭이'] #unicode type 을 저장하고 있는 list

# tuple type (list type의 read only 버전 읽기전용리스트 수정삭제를 염두하지않기에 속도가 빠르다.)
nums2 =(10, 20, 30, 40, 50)
names2 = ('kim', 'lee', 'park')
friends2 = (u'김구라', u'해골', u'원숭이')

# dict type  (""를 생략 할수 없다. javascript의 object 와 비슷하다.)
mem1 = {"num":1, "name":u"김구라", "isMan":True}
mem2 = {"num":2, "name":u"해골", "isMan":False}

# function type (javascript에서는 function a(){} 이렇게 만들었지만 python은 영역을 :과 들여쓰기로한다.) 
def a(): 
    pass #(pass 는 함수의 빈영역을 표시할때 쓴다.)

def b(): #(b()줄과 print 앞글자 줄이 들여쓰기로 맞아야한다.  )
    print 'one'
    print 'two'
    print 'three'

# b 라는 함수 호출
b()

# b 함수의 참조 값을 c 에 대입 
c=b #c 와 b는 같은 함수, c를 호출하면 b의 함수가 호출됨. 

# None type
emptyVar = None # java 의 null 이라고 이해 하면 된다.



print "Step02_DataType.py 가 종료 됩니다."








