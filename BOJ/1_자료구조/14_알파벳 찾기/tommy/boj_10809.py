from sys import stdin

answer = []
in_str = stdin.readline().rstrip()
# a부터 z까지 loop를 돌린다.
for i in range(ord('a'), ord('z') + 1):
    try:
        # str.index를 할 경우, 최초에 나타난 위치를 가르키므로 answer에 삽입한다.
        answer.append(str(in_str.index(chr(i))))
    except ValueError:
        # ValueError가 나올 경우, 존재하지 않으므로 -1을 리턴한다.
        answer.append('-1')

print(' '.join(answer))