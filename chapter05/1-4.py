def recursive_function(i):
    if i==100:
        return
    print(i, '%d번째 재귀함수 호출'%i)
    recursive_function(i+1)
recursive_function(1)