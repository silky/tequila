from openvqe.circuit import *
from openvqe.objective import Objective
from openvqe.gates import *
from numpy import pi

if __name__ == "__main__":

    gate=Ry(target=1,control=3,angle=pi/3,phase=1.0,frozen=False)

    gradient=gate.gradient()
    print("gradient at of Ry at gate level", gradient)


    ac = QCircuit()
    ac += X(target=0,control=None)
    ac += Ry(target=1, control=None, angle=pi / 2)

    obj= Objective(ac,observable=None)
    gradient = obj.gradient()

    print("gradient of X, Ry at objective level", gradient)

    ac = QCircuit()
    ac += X(target=0,power=2.3,phase=-1.0)
    ac += Ry(target=1, control=0, angle=pi / 2)


    print('gradient of Xpower, controlled Ry at circuit level:', ac.gradient())
    obj= Objective(ac,observable=None)
    gradient = obj.gradient()

    print("gradient of Xpower controlled Ry at objective level", gradient)

    ac = QCircuit()
    ac += X(0)
    ac += Rx(target=2, angle=0.5,frozen=True)
    ac += Ry(target=1, control=0, angle=pi / 2)
    ac += Rz(target=1, control=[0,2], angle=pi / 2)

    obj= Objective(ac,observable=None)
    gradient = obj.gradient()

    print("gradient at objective level", gradient)