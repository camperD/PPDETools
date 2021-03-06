# ========== Grids.py ==========

# ===== Imports =====
import numpy as np


class Grid1D:
    """
    class - Grid1D

    A one-dimmensional finite grid. Offers varying types of grids, including
    cell-edge and cell-centered, both with options for grid points. Points are
    stored in an NumPy array object. Includes iterator functionality for ease
    in accessing or changing grid points via a for loop.
    """

    def __init__(self, lBound, rBound, NPTS, grid_type='cell edge'):
        self._lBound = lBound
        self._rBound = rBound
        self._NPTS = NPTS
        self._index = -1

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
        """
        Function: __iter__

        Iterator function for Grid1D
        """

        return self

    def __next__(self):
        """
        Function: __next__

        Allows for Grid1D to be iteratored through. Iterates through the grid
        points within the grid, starting from the left bound and iterating to
        the right end.
        """
        if (self._index == self._NPTS-1):
            raise StopIteration
        self._index = self._index + 1
        return self._pts[self._index]

    # ----- Accessor Functions -----
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


# ===== END OF CLASS Grid1D =====


class Grid2D:
    """
    class - Grid2D

    A two-dimmensional finite grid. Employs NumPy's meshgrid to create a two
    dimmensional grid. Creates and stores Grid1D objects for the X and Y grids.
    """

    def __init__(self, xBounds, yBounds, NPTSX, NPTSY, grid_type='cell edge'):
        self._xLow = xBounds[0]
        self._xUp = xBounds[1]
        self._yLow = yBounds[0]
        self._yUp = yBounds[1]
        self._NPTSX = NPTSX
        self._NPTSY = NPTSY
        self._XGrid = Grid1D(self._xLow, self._xUp, self._NPTSX,
                             grid_type=grid_type)
        self._YGrid = Grid1D(self._yLow, self._yUp, self._NPTSY,
                             grid_type=grid_type)
        self._XPts, self._YPts = np.meshgrid(self._XGrid.getPoints(),
                                             self._YGrid.getPoints())

    # ----- Accessor Functions -----
    def getX(self):
        return self._XPts

    def getY(self):
        return self._YPts

    def getNPTSX(self):
        return self._NPTSX

    def getNPTSY(self):
        return self._NPTSY


# ===== END OF CLASS Grid2D =====


# ========== END OF Grids.py ==========
