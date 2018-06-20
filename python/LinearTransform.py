class LinearTransform(object):
    def __init__(self, filename): 
        self.data = np.load(filename)
        # inefficient but the only way I could quickly figure out how to do this
        self.Y = self.data
    
    def reset(self):
        self.Y = self.data
        return(self)
    
    def stretch(self, a, b=None):
        """Linear Transformation: Stretch
        Compute the stretched version of an image, with matrix [[a, 0], [0, b]]
        If a=b, then it is a dilation
        """
        if b is None:
            b = a
        X = np.array([[a, 0], [0, b]])
        self.Y = X.dot(self.Y)
        return(self)
         
    def shear(self, a, horizontal=True):
        """Linear Transformation: Shear
        Slants the vector by a scalar factor horizontally (x-axis) or vertically (y-axis). 
        """
        if horizontal:
            X = np.array([[1, a], [0, 1]])
        else:
            X = np.array([[1, 0], [a, 1]])
        self.Y = X.dot(self.Y)
        return(self)

    def reflection(self, a, b):
        """Linear Transformation: Reflection
        Reflects the vector about a line that passes through the origin
        """
        X = np.array([[a**2 - b**2, 2*a*b], [2*a*b, b**2 - a**2]])/(a**2 + b**2)
        self.Y = X.dot(self.Y)
        return(self)

    def plot(self, aspect=None):
        plt.plot(self.Y[0], self.Y[1], 'k,')
        if aspect:
            plt.gca().set_aspect(aspect)
        plt.show()
#        self.reset()
