import numpy as np

P, N, M = map(int,input().split())
A = np.array([input().split() for x in range(P)],int)
B = np.array([input().split() for x in range(N)],int)
print(np.concatenate((A, B), axis = 0))


