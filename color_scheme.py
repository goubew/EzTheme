from color import Color

class ColorScheme:
    """Holds a number of colors that describe the theme"""
    def __init__(self, rawColors = None):
        if rawColors is None:
            self.colors = {}
            self.colors["black"] = Color("black", "00", "00", "00")
            self.colors["black2"] = Color("black", "00", "00", "00")
            self.colors["red"] = Color("black", "00", "00", "00")
            self.colors["red2"] = Color("black", "00", "00", "00")
            self.colors["green"] = Color("black", "00", "00", "00")
            self.colors["green2"] = Color("black", "00", "00", "00")
            self.colors["yellow"] = Color("black", "00", "00", "00")
            self.colors["yellow2"] = Color("black", "00", "00", "00")
            self.colors["blue"] = Color("black", "00", "00", "00")
            self.colors["blue2"] = Color("black", "00", "00", "00")
            self.colors["magenta"] = Color("black", "00", "00", "00")
            self.colors["magenta2"] = Color("black", "00", "00", "00")
            self.colors["cyan"] = Color("black", "00", "00", "00")
            self.colors["cyan2"] = Color("black", "00", "00", "00")
            self.colors["white"] = Color("black", "00", "00", "00")
            self.colors["white2"] = Color("black", "00", "00", "00")
        else:
            for line in rawColors:
                components = line.split(",")
                self.colors[components[0]] = Color(components[1], components[2], components[3])

    def toString(self):
        """Returns a string representation of all of the colors"""
        result = ""
        result += ("black," + self.colors["black"].toFullString() + "\n")
        result += ("black2," + self.colors["black2"].toFullString() + "\n")
        result += ("red," + self.colors["red"].toFullString() + "\n")
        result += ("red2," + self.colors["red2"].toFullString() + "\n")
        result += ("green," + self.colors["green"].toFullString() + "\n")
        result += ("green2," + self.colors["green2"].toFullString() + "\n")
        result += ("yellow," + self.colors["yellow"].toFullString() + "\n")
        result += ("yellow2," + self.colors["yellow2"].toFullString() + "\n")
        result += ("blue," + self.colors["blue"].toFullString() + "\n")
        result += ("blue2," + self.colors["blue2"].toFullString() + "\n")
        result += ("magenta," + self.colors["magenta"].toFullString() + "\n")
        result += ("magenta2," + self.colors["magenta2"].toFullString() + "\n")
        result += ("white," + self.colors["white"].toFullString() + "\n")
        result += ("white2," + self.colors["white2"].toFullString() + "\n")
        return result

    def setSingleColor(self, name, color):
        """Sets a color within the color dictionary"""
        self.colors[name] = color
        print("Set color " + name + " to " + color.toFullString())

    def setDoubleColors(self, name, color):
        self.setSingleColor(name, color)
        self.setSingleColor( (name + "2"), color)
