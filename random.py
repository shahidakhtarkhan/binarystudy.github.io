>>> import numpy as np
>>> np.random.seed(0)
>>> np.random.randint(3)
0
>>> np.random.seed(0)
>>> np.random.rand(3)
array([ 0.5488135 ,  0.71518937,  0.60276338])
>>> np.random.seed(0)
>>> np.random.rand(3)
array([ 0.5488135 ,  0.71518937,  0.60276338])
>>> np.random.seed(1)
>>> np.random.rand(3)
array([  4.17022005e-01,   7.20324493e-01,   1.14374817e-04])
>>> np.random.seed(1)
>>> np.random.rand(3)
array([  4.17022005e-01,   7.20324493e-01,   1.14374817e-04])
>>> np.random.seed(2)
>>> np.random.rand(3)
array([ 0.4359949 ,  0.02592623,  0.54966248])
>>> np.random.seed(2)
>>> np.random.rand(3)
array([ 0.4359949 ,  0.02592623,  0.54966248])
>>> 
