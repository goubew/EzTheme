from theme_component import BspwmTheme
from theme_component import LemonbarTheme
from theme_component import UrxvtTheme
from color_scheme import ColorScheme
from color import Color
import os

class Theme():
    """A class that loads and saves a save in all the places needed"""

    def __init__(self, scheme):
        """Saves the color scheme for use with the components"""
        #Associated scheme
        self.scheme = scheme
        #A list of theme components
        self.themeComponents = [BspwmTheme(), LemonbarTheme(), UrxvtTheme()]

    def writeTheme(self):
        """Writes out each of the components's config files"""
        for theme in self.themeComponents:
            theme.saveTheme(scheme)

    def loadThemeBackup(self, path):
        """loads a theme backup file from a path"""
        if os.path.isfile(path):
            lines = [line.rstrip('\n') for line in open(path, "r")]
            self.scheme = ColorScheme(lines)
        else:
            print("The file" + path + " could not be found")

    def saveThemeBackup(self, path):
        """saves a theme to a backup file at the path"""
        out = open(path, 'w')
        out.write(self.scheme.toString())
        out.close()

if __name__ == "__main__":
    """load the theme, set the colors and execute it"""
    scheme = ColorScheme()
    scheme.setDoubleColors("white", Color("white", "f0", "f0", "f0"))
    scheme.setSingleColor("black", Color("dark-blue", "39", "49", "52"))
    scheme.setSingleColor("black2", Color("grey", "70", "83", "8c"))
    scheme.setDoubleColors("red", Color("dull-red", "99", "73", "6e"))
    scheme.setDoubleColors("green", Color("dull-green", "78", "a0", "90"))
    scheme.setDoubleColors("yellow", Color("dull-yellow", "bf", "b7", "a1"))
    scheme.setDoubleColors("blue", Color("dull-blue", "7c", "9f", "a6"))
    scheme.setDoubleColors("magenta", Color("dull-magenta", "bf", "9c", "86"))
    scheme.setDoubleColors("cyan", Color("dull-cyan", "99", "bf", "ba"))

    theme = Theme(scheme)
    theme.writeTheme()
