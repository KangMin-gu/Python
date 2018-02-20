#-*- coding:utf-8 -*- 

nameSet={'kim', 'park', 'lee'}

result1= 'kim' in nameSet
result2= 'kim' not in nameSet

print "result1 :", result1
print "result2 :", result2

#list 에서 중복을 제거할때 사용할 수 있다.
nums=[10,10,20,20,30,30,40,50]

# 빌트인 set 클래스를 이용해서 중복 제건된 set 얻어내기 
set1=set(nums) # set 객체 생성  
#파이썬은 생성자 호출할대 자바처럼 new할 필요없다. 

print set1

# 빌트인 list 클래스를 이용해서 set 을 list 로 얻어내기
nums2=list(set1)

print "num2:", nums2

# 정렬
nums2.sort()
print "정렬후 nums2"
print nums2

# 역순정렬
nums2.sort(reverse=True)
print "역순정렬후 nums2"
print nums2


print "Step07_set2.py 가 종료 됩니다."
