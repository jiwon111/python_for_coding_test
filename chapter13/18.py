p = input()

def balanced_index(p):
    left_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_cnt += 1
        else:
            left_cnt -= 1
        if left_cnt == 0:
            return i

#올바른 괄호 문자열인지 판단
def check_proper(p):
    left_cnt = 0
    for i in p:
        if i == '(':
            left_cnt += 1
        else:
            if left_cnt == 0:#쌍이 맞지 않는 경우
                return False
            left_cnt -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)

    u = p[:index+1]
    v = p[index+1:]

    #올바른 괄호 문자열이면 v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u+solution(v)
    #올바른 괄호 문자열이 아니라면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])#첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)
    return answer

print(solution(p))