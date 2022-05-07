def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]
 
def bruteforce01(p, w, m):
    if len(p) == len(w):
        n = len(p)
        bit_strings = get_strings(n)
        max_profit = 0
        solution = ''

        for s in bit_strings:
            profit = sum([int(s[i]) * p[i] for i in range(n)])
            weight = sum([int(s[i]) * w[i] for i in range(n)])
        
            if weight <=m and profit > max_profit:
                max_profit = profit
                solution = s
        
        return (solution, max_profit)
    else:
        raise Exception("Length of cost and weight list should be equal")

def bruteforcefractional(p, w, c):
    if len(p) == len(w):
        n = len(p)
        max_profit = 0
        bit_strings = get_strings(n)
        for b in bit_strings:
            i1 = [i for i,x in enumerate(b) if x == '1']
            i0 = [i for i,x in enumerate(b) if x == '0']
            profit_whole = 0
            weight_whole = 0
            for i in i1:
                profit_whole += p[i]
                weight_whole += w[i]
            max_fractional_profit = 0
            if weight_whole < c :
                for i in i0:
                    ratio = (w[i], c - weight_whole )[(c - weight_whole < w[i])] 
                    fractional_profit = (p[i]/w[i])*ratio
                    if fractional_profit > max_fractional_profit:
                        max_fractional_profit = fractional_profit
            total_profit = max_fractional_profit + profit_whole
            if weight_whole <= c and total_profit >= max_profit:
                max_profit = total_profit
        return max_profit
    else:
        raise Exception("Length of cost and weight list should be equal")

def greedyfractional(profit, weight, m):
    if len(profit) == len(weight):
        n = len(profit)
        index = list(range(n))
    
        ratio = [0] * n
        for z in range(n):
            ratio[z] = profit[z] / weight[z]
        index.sort(key=lambda i: ratio[i], reverse=True)
    
        max_profit = 0
        for i in index:
            if weight[i] <= m:
                max_profit += profit[i]
                m -= weight[i]
            else:
                max_profit += profit[i] * (m/weight[i])
                break
    
        return max_profit
    else:
        raise Exception("Length of cost and weight list should be equal")


def dynamic01(p, w, m): 
    if len(w) == len(p):
        n = len(p)
        arr = [[0 for x in range(m + 1)] for x in range(n + 1)] 
    
        for i in range(n + 1): 
            for j in range(m + 1): 
                if i == 0 or w == 0: 
                    arr[i][j] = 0
                elif w[i-1] <= j : 
                    arr[i][j] = max(p[i-1] + arr[i-1][j-w[i-1]], arr[i-1][j]) 
                else: 
                    arr[i][j] = arr[i-1][j] 
    
        return arr[n][m] 
    else:
        raise Exception("Length of cost and weight list should be equal")


profit = [10,20,60,100,90]
weight = [8,5,10,7,11]
# print(bruteforce(profit,weight,15))
# print(bruteforcefractional(profit,weight,15))
print(dynamic01(profit, weight,15))