text = input()
valid_text = ''

# text를 while 루프 돌릴 경우, 입력 받은 text의 크기가 0이 될 때 까지 loop를 수행한다.
while text:
    # 문제에서 < 태그가 오면 다음에 > 태그가 무조건 오기 때문에 태그 블록 단위로 처리를 하기 위해 태그 시작 인덱스와 끝 인덱스를 반환하도록 하였다.
    start = text.find('<')
    end = text.find('>')

    # 만약 태그가 있을 경우 -1이 아닌 0이상의 정수를 반환하기 때문에 태그가 있을 경우를 처리한다.
    if start != -1:
        # <open>tag test<close> 을 예로 들면,
        # 첫번째 태그 <open>은 start: 0, end: 5 이므로 첫 번째 루프에서 text[:start] == text[:0] 이므로
        # 태그 앞에 있던 공백 글자 '' + text[0:5 + 1]를 반환하여 '' + '<open>'를 valid_text에 넣는다.
        # text엔 <open> 다음 문자열인 tag<close>를 넣어서 다시 loop를 돌린다.

        # 두번째 루프에서는 tag<close> 에서 tag를 처리해주는데, tag test를 먼저 선처리한다.
        # tag test는 스플릿하여 ['tag', 'test'] 형태의 리스트로 반한되는데 람다식으로 각 원소를 x[::-1] 하게 된다면 원소를 뒤집을 수 있게 되므로
        # ['gat', 'tset']를 반환하여 join -> 'gat tset' + <close> 가 valid_text에 추가되며, text의 크기가 0이 되어 loop가 종료된다.
        print(text[:start].split())
        valid_text += ' '.join(list(map(lambda x: x[::-1], text[:start].split()))) + text[start:end + 1]
        text = text[end + 1:]
    else:
        # 만약 태그가 없다면 위와 동일한 처리를 하지만, 태그를 다는 부분만 제외하고 단어를 뒤집은 다음에 loop를 종료시킨다.
        valid_text += ' '.join(list(map(lambda x: x[::-1], text.split())))
        break

print(valid_text)