#!/usr/bin/python3.6

import cProfile
import numpy as np
from scipy import signal

def startA (n):
    # np.diag maybe?
    A = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            A[i][j] = 10
    for i in range(n):
        A[0, i] = 100
        A[1, i] = 100

    Anew = A.copy()

    return A, Anew

def makeMV(Anew, A, n):
    # Spróbować wyciągnąć 1/4 przed całą macierz
    #for i in range(1, n-1):
    #    for j in range(1, n-1):
    #        Anew[i, j] =       (A[i-1, j  ] \
    #                          + A[i+1, j  ] \
    #                          + A[i  , j-1] \
    #                          + A[i  , j+1])
    #Anew[1:n-1, 1:n-1] *= 0.25
    # Define kernel for convolution                                         
    kernel = np.array([[0,1,0],
                       [1,0,1],
                       [0,1,0]])
    # Perform 2D convolution with input data and kernel 
    Anew[1:n-1, 1:n-1] = signal.convolve2d(A, kernel, mode="valid")*.25

def error(A,Anew):
#	err = 0
#	for i in range(1,n-1):
#		for j in range(1,n-1):
#			pom = np.abs(A[i,j]-Anew[i,j])
#			if pom > err: err = pom
#	return err
    return np.abs(A-Anew).max()

def copy(A, Anew, n):
    # zastąpić biblioteczną funkcją numpy/[deep]copy
    # macierze numpy mają metodę copy() robiącą to szybko
    for i in range(1,n-1):
        for j in range(1,n-1):
            A[i,j] = Anew[i,j]

pr = cProfile.Profile()
pr.enable()

n = 100

A, Anew = startA(n)

for i in range(1000):
    makeMV(Anew, A, n)

    err = error(A, Anew)
# print(Anew)
    #copy(A, Anew, n)
    A = Anew.copy()

    if i%100 == 0: print(err)

pr.disable()
pr.print_stats(sort='time')
