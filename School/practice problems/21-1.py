def lenFun(arg):
    """문자열과 리스트의 길이를 재는 함수"""
    count = 0
    for _ in arg:
        count += 1
    return count

def search_word(arg_word):
    """문자열에서 해당 단어를 찾아 리스트로 반환하는 함수"""
    word_len = lenFun(arg_word)
    answer_list = []
    
    for i in range(lenFun(SENTENCE) - word_len + 1):
        # 유저가 입력한 단어와 길이가 일치하는지 확인
        if not ((i == 0 or SENTENCE[i - 1] == " " or SENTENCE[i - 1] == "\n") and (i + word_len >= lenFun(SENTENCE) or SENTENCE[i + word_len] == " " or SENTENCE[i + word_len] == "\n")):
            continue
        isEqual = True
        # 유저가 입력한 단어와 일치하는지 확인
        for j in range(word_len):
            if arg_word[j] != SENTENCE[i + j]:
                isEqual = False
                break
        
        if isEqual:
            answer_list.append(i)

    return answer_list

def getCount():
    """단어의 개수를 세는 함수"""
    word = []
    word_count = 0  # 단어의 개수
    alp_count = 0   # 문자의 개수
    line_count = 1  # 줄의 개수
    for i in range(lenFun(SENTENCE)):
        if SENTENCE[i] != " " and SENTENCE[i] != "\n":
            word.append(SENTENCE[i])
            alp_count += 1
        else:
            if SENTENCE[i] == "\n":
                line_count += 1
            if lenFun(word) != 0:
                word = []
                word_count += 1
    
    # 마지막에 단어가 남아있으면 +1
    if lenFun(word) != 0:
        word_count += 1
    
    return word_count, alp_count, line_count

SENTENCE = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

while True:
    input_word = input("검색할 문자열을 입력하세요: ")

    # 검색 결과가 없는 경우
    find_word_list = search_word(input_word)
    if lenFun(find_word_list) == 0:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
        continue

    count = getCount()

    print(f"검색된 문자열의 개수: {lenFun(find_word_list)}")
    print(f"검색된 문자열의 위치: {find_word_list}")
    print(f"단어의 개수: {count[0]}")
    print(f"전체 문자 수: {count[1]}")
    print(f"줄 수: {count[2]}")
    break