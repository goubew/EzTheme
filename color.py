class Color:
    """A class that holds an RGB color"""
    def __init__(self, name, R, G, B):
        self.name = name
        self.R = R
        self.G = G
        self.B = B
    
    def toRawString(self):
        """Returns the color as an RGB string"""
        return self.R + self.G + self.B

    def toColorString(self):
        """Returns the color as an #RGB string"""
        return "#" + self.toRawString()

    def toFullString(self):
        """Returns the color in a csv savable format"""
        return (self.name + "," + self.R + "," + self.G + "," + self.B)
