# 1209. [S/W 문제해결 기본] 2일차 - Sum
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE

n=100
def sumLine(array,sr,sc,dr,dc):
    sumcount=0
    for i in range(n):
        sumcount+=array[sr+dr*i][sc+dc*i]
    return sumcount
def myMax(li):
    maximum=0
    for i in li:
        maximum=i if i>maximum else maximum
    return maximum
for tc in range(1,11):
    input()
    array=[list(map(int,input().split())) for _ in range(n)]
    result=[]
    for i in range(n):
        result.append(sumLine(array,i,0,0,1))
        result.append(sumLine(array,0,i,1,0))
    result.append(sumLine(array,0,0,1,1))
    result.append(sumLine(array,0,-1,1,-1))
    print(f"#{tc} {myMax(result)}")