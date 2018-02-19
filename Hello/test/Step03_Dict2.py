#-*- coding:utf-8 -*- 

#회원 한명의 정보를 dict 에 담기

mem1={"num":1, "name":u"김구라", "addr":u"노량진"}

# dict 의 모든 key 값을 list로 얻어내기
result = mem1.keys() #mem1의 키값을 리스트에 담아 반환한다. 

# dict 에 담긴 모든 내용을 콘솔에 출력해 보기
for tmp in mem1.keys():
    print tmp, " : ", mem1[tmp]