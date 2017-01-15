def dynamiCoins(coinList,change,minCoins):
    for cents in range(change+1):
        coinCount=cents
        for j in [c for c in coinList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
        minCoins[cents]=coinCount
    return minCoins[change]
print(dynamiCoins([1,5,10,25],37,[0]*38))
