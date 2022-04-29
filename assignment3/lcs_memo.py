X = "president"
Y = "providence"
Memo = [[None for i in range(len(Y)+1)] for j in range(len(X)+1)]
# for x in Memo:
#     print(x)

def LCS_memo(X,Y,m,n,Memo):
    if Memo[m][n] != None:
        return Memo[m][n]
    elif m == len(X) or n == len(Y):
        result = 0
    elif X[m] == Y[n]:
        result =  1 + LCS_memo(X,Y,m+1,n+1,Memo)
    else:
        result = max(LCS_memo(X,Y,m+1,n,Memo),LCS_memo(X,Y,m,n+1,Memo))
    Memo[m][n] = result
    return result

print(LCS_memo(X,Y,0,0,Memo))