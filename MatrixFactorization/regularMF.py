# author: wanghao
# regularization matrix factorization
import numpy as np

def regularMF(R,W,H,K,step=5000,alpha=0.001,lamda=0.02):
    print "regularization matrix factorization function"

    for iter in xrange(step):
        for row in xrange(len(R)):
            for col in xrange(len(R[0])):
                if R[row][col] > 0 :
                    # calculate loss
                    err_i_j = R[row][col] - np.dot(W[:,row],H[:,col].T)
                    for i in xrange(K):
                        W[i][row]= W[i][row] - alpha*(-2*err_i_j*H[i][col] + lamda*W[i][row])
                        H[i][col] = H[i][col] - alpha*(-2*err_i_j*W[i][row] + lamda*H[i][col])

        error = 0
        for row in xrange(len(R)):
            for col in xrange(len(R[0])):
                if R[row][col] > 0 :
                    error = error + R[row][col] - np.dot(W[:,row], H[:,col].T)
                    for i in xrange(K):
                        error = error + (lamda / 2) *(pow(W[i,row], 2) + pow(H[i,col], 2))
        if iter % 100 == 0 :
            print "iter=",iter,'error is ', error


    return W, H


if __name__ == '__main__':
    print "Main Function ..."
    print '*'*50

    print "make data ..."
    row = 5
    col = 4

    #np.random.seed(0);
    #data = np.random.rand(row,col)
    data = [[5,3,0,1],
            [4,0,0,1],
            [1,1,0,5],
            [1,0,0,4],
            [0,1,5,4],]

    for i in xrange(len(data)):
        print data[i]

    print "*"*50

    K = 2
    print "latent diemenon is ",K
    print '*'*50

    print "random for sub matrix W and H ..."
    W = np.random.rand(K,row)
    H = np.random.rand(K,col)

    print "calculate the matrix factorization ..."
    finalW,finalH = regularMF(data, W, H, K)

    print 'final result ...'
    finaldata = np.dot(finalW.T,finalH)
    for i in xrange(len(finaldata)):
        print finaldata[i]
