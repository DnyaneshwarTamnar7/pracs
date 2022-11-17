def printsolution(b,N):
    for i in range(N):
        for j in range(N):
            print(b[i][j],end=" ")
        print()

def isSafeboard(b,row,col,N):
    for i in range(col):
        if b[row][i]==1:
            return False
        
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if b[i][j]==1:
            return False
    for i,j in zip(range(row,N,1), range(col,-1,-1)):
        if b[i][j]==1:
            return False
    return True

def sloveNQUtil(b,col,N):
    if col>=N:
        return True
    
    for i in range(N):
        if isSafeboard(b,i,col,N):
            b[i][col]=1
            if sloveNQUtil(b,col+1,N)==True:
                return True
            b[i][col]=0
    return False

def sloveNQ():
    N = int(input("Enter Board Size"))
    b = [[0 for i in range(N)] for i in range(N)]
    if sloveNQUtil(b,0,N) == False:
        print("Solution does not find")
        return False
    printsolution(b,N)
    return True

sloveNQ()