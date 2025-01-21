import sys
input = sys.stdin.readline


def Teams(N, M, K):
    fTeams = N // 2 #fTeams는 여자를 둘씩 나눴을 때 몫
    if (M > fTeams): #남자가 남을 때
        mTeams = fTeams
        notTeams = M - mTeams
        if(K > notTeams):
            while(K <= notTeams):
                notTeams += 3
                fTeams -= 1
            print(fTeams)
        else :
            print(fTeams)
        
    else : #여자가 남을 때
        mTeams = M
        notTeams = N - 2 *fTeams
        if (K > notTeams):
            while(K <= notTeams):
                notTeams += 3
                mTeams -= 1
            print(mTeams)
        else:
            print(mTeams)

N, M, K = map(int, input().split())
Teams(N, M, K)
