import re #파이썬 정규 표현식 사용 위한 내장 모듈
def del_vowels(my_str):
    for letter in my_str:
        result = re.sub("[a,e,i,o,u,A,E,I,O,U]","",my_str) #re.sub은 re 모듈 함수
    return result

my_str = input("my_str = ")
print(del_vowels(my_str))

'''정규 표현식은 문자열에서 특정 문자 또는 문자열이 존재하는지, 
어느 위치에 있는지 쉽게 알 수 있게 해준다.
특히 이번에 쓴 re.sub 함수는 특정 패턴을 원하는 문자열로 교체해준다. 
re.sub(교체할 패턴,어떤 것으로 교체할건지, 교체할 해당 문자열, 최대 몇 개 교체할 것인지) 
넣어서 사용한다'''
