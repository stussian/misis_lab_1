k = int(input())
och = 0
zaoch = 0
for i in range(0, k):
    n = list(map(str, input().split()))
    if 'True' in n:
        och += 1
    else:
        zaoch += 1
print(och, zaoch)