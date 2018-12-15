# ========== Grids.py ==========
import numpy as np
import matplotlib.pyplot as plt


class Grid1D:

    def __init__(self, lBound, rBound, NPTS, grid_type='cell edge'):
        self._lBound = lBound
        self._rBound = rBound
        self._NPTS = NPTS
        self._index = 0

        if (grid_type == 'cell edge'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS - 1)
            self._pts = np.linspace(self._lBound,
                                    self._rBound,
                                    num=self._NPTS)
        elif (grid_type == 'cell centered'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS)
            self._pts = np.linspace(self._lBound + self._delX/2,
                                    self._rBound - self._delX/2,
                                    num=self._NPTS)
        elif (grid_type == 'cell edge gp'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS - 1)
            self._pts = np.linspace(self._lBound - self._delX,
                                    self._rBound + self._delX,
                                    num=self._NPTS)
        elif (grid_type == 'cell centered gp'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS)
            self._pts = np.linspace(self._lBound - self._delX/2,
                                    self._rBound + self._delX/2,
                                    num=self._NPTS)
        else:
            print("ERROR IN Grid1D: INVALID grid_type NAME")

    def __iter__(self):
        return self

    def __next__(self):
        if (self._index == self._NPTS-1):
            raise StopIteration
        self._index = self._index + 1
        return self._pts[self._index]

    def getRBound(self):
        return self._rBound

    def getLBound(self):
        return self._lBound

    def getNPTS(self):
        return self._NPTS

    def getDelX(self):
        return self._delX

    def getPoints(self):
        return self._pts


# --- END OF CLASS Grid1D ---

# -- BEGIN TESTING/DEBUGGING SECTION ---

# Grid spacing visualization
grid1 = Grid1D(0, 1, 10, grid_type='cell edge')
grid2 = Grid1D(0, 1, 10, grid_type='cell centered')
grid3 = Grid1D(0, 1, 10, grid_type='cell edge gp')
grid4 = Grid1D(0, 1, 10, grid_type='cell centered gp')

for point in grid1:
    print(point)

x1 = grid1.getPoints()
x2 = grid2.getPoints()
x3 = grid3.getPoints()
x4 = grid4.getPoints()

y1 = np.zeros(10) + 1
y2 = np.zeros(10) + 2
y3 = np.zeros(10) + 3
y4 = np.zeros(10) + 4

plt.plot(x1, y1, 'r.', x2, y2, 'b.', x3, y3, 'g.', x4, y4, 'y.')
plt.legend(['Cell-Edge',
            'Cell-Centered',
            'Cell-Edge w/ GP',
            'Cell-Centered w/ GP'],
           loc='lower left',
           bbox_to_anchor=(.2, 1.00),
           borderaxespad=0.5,
           ncol=2)
plt.show()

# --- END OF TESTING/DEBUGGING SECTION ---

# ========== END OF Grids.py ==========
