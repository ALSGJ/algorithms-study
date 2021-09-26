s = input()

# 알파벳 a부터 z까지 숫자 카운트를 위해 dictionary 자료구조 형태로 초기화한다.
# {a: 0, b: 0, c: 0, ... z: 0}
s_dict = {chr(i): 0 for i in range(97, 123)}

# s_dict에 해당되는 알파벳에 대해 증분시켜준다.
for a in s:
    s_dict[a] += 1

# 값만 가져와 문자열 형태로 반환한다.
print(' '.join(map(str, (s_dict.values()))))