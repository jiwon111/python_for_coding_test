def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2+1):
        compressed=""
        prev = s[0:step]#앞에서부터 step만큼의 문자열 추출
        cnt = 1

        #step만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            #이전 상태와 동일하다면 cnt 증가
            if prev == s[j:j+step]:
                cnt+=1
            #다른 문자열이 나왔다면
            else:
                compressed += str(cnt)+prev if cnt>=2 else prev
                prev = s[j:j+step]
                cnt=1

        compressed += str(cnt)+ prev if cnt>=2 else prev

        answer = min(answer, len(compressed))
    return answer