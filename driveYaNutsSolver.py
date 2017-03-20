a = [1,4,3,6,5,2]
b = [1,6,5,4,3,2]
c = [1,6,4,2,5,3]
d = [1,6,2,4,5,3]
e = [1,6,5,3,2,4]
f = [1,4,6,2,3,5]
g = [1,2,3,4,5,6]
answer = [a,b,c,d,e,f,g]
#answer = [1,2,3,4,5,6,7]
# print a + b + c + d + e + f + g
# print answer

def firstAndNext(x, y, i):
    y = y[y.index(x[i]):] + y[:y.index(x[i])]
    return y


for z in range(7):
    i=1
    ran = 6
    for u in range(6):
        for y in range(ran):
            for x in range(1,7):
                answer[x] = firstAndNext(answer[0], answer[x], x-1)
            #print (answer[1][1] , answer[6][5] , answer[1][5] , answer[2][1] , answer[2][5] , answer[3][1] , answer[3][5] , answer[4][1] , answer[4][5] , answer[5][1], answer[5][5], answer[6][1])
            if (answer[1][1] == answer[6][5] and answer[1][5] == answer[2][1] and answer[2][5] == answer[3][1] and answer[3][5] == answer[4][1] and answer[4][5] == answer[5][1] and answer[5][5] == answer[6][1]):
                print 'true'
            #print answer
            answer.insert(i,answer.pop())
        i += 1
        ran -= 1
    answer.insert(0,answer.pop())
