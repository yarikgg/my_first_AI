import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(JAVA, error, python):
    x = np.array([JAVA, error, python])
    w1 = [0.3, 0.3, 0]
    w2 = [0.4, -0.5, 1]
    weight1 = np.array([w1, w2])
    weight2 = np.array([-1, 1])

    inp = np.dot(weight1, x)

    out = np.array([act(x) for x in inp]) 

    end = np.dot(weight2, out)
    y = act(end)
    print('output: '+str(y))

    return y 

JAVA = 1
error = 0
python = 1

res = go(JAVA, error, python)
if res == 1:
    print('да')
else:
    print('error')