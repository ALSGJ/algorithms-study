t = int(input())

for _ in range(t):
    sentence = input().split()
    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]
    print(' '.join(sentence))
