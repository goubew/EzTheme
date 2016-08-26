from abc import ABC, abstractmethod
import os

class ThemeComponent(ABC):
    """An abstract class with methods to save a color theme for a specific program"""

    @abstractmethod
    def saveTheme(self, scheme):
        pass

class BspwmTheme(ThemeComponent):
    """An instantiation of the ThemeComponent class. Used to write a theme to BSPWM files"""

    #The config file location
    bspwmLoc = "/home/statue/theme/bspwm.bash"

    def saveTheme(self, scheme):
        """writes to the bspwm config file"""
        bspwmFile = open(self.bspwmLoc, 'w')

        bspwmFile.write("#!/bin/bash")

        bspwmFile.write("\nbspc config focused_border_color \"" + scheme.colors["white"].toColorString() + "\"")

        bspwmFile.write("\nbspc config active_border_color \"" + scheme.colors["white"].toColorString() + "\"")

        bspwmFile.write("\nbspc config normal_border_color \"" + scheme.colors["black"].toColorString() + "\"")
        
        bspwmFile.close()

class LemonbarTheme(ThemeComponent):
    """An instantiation of the ThemeComponent class. Used to write a theme to lemonbar files"""

    #The config file location
    lemonbarLoc = "/home/statue/theme/lemonbar.bash"

    def saveTheme(self, scheme):
        """writes to the bspwm config file"""
        lemonbarFile = open(self.lemonbarLoc, 'w')
        
        lemonbarFile.write("#!/bin/bash")

        lemonbarFile.write("\nforeground=\"" + scheme.colors["white"].toColorString() + "\"")

        lemonbarFile.write("\nbackground=\"" + scheme.colors["black"].toColorString() + "\"")

        lemonbarFile.close()

class UrxvtTheme(ThemeComponent):
    """An instantiation of the ThemeComponent class. Used to write a theme to urxvt files"""
    
    #The config file location
    urxvtLoc = "/home/statue/theme/urxvt"

    def urxvtLine(self, value, scheme, schemeColor):
        result = "*." + value + ": "
        result += scheme.colors[schemeColor].toColorString()
        return result

    def saveTheme(self, scheme):
        """writes to the urxvt config file"""
        urxvtFile = open(self.urxvtLoc, 'w')

        urxvtFile.write("#!bin/bash")

        urxvtFile.write("\n!special")
        urxvtFile.write("\n" + self.urxvtLine("foreground", scheme, "white"))
        urxvtFile.write("\n" + self.urxvtLine("background", scheme, "black"))
        urxvtFile.write("\n" + self.urxvtLine("cursorColor", scheme, "white"))

        urxvtFile.write("\n!black")
        urxvtFile.write("\n" + self.urxvtLine("color0", scheme, "black"))
        urxvtFile.write("\n" + self.urxvtLine("color8", scheme, "black2"))

        urxvtFile.write("\n!red")
        urxvtFile.write("\n" + self.urxvtLine("color1", scheme, "red"))
        urxvtFile.write("\n" + self.urxvtLine("color9", scheme, "red2"))

        urxvtFile.write("\n!green")
        urxvtFile.write("\n" + self.urxvtLine("color2", scheme, "green"))
        urxvtFile.write("\n" + self.urxvtLine("color10", scheme, "green2"))

        urxvtFile.write("\n!yellow")
        urxvtFile.write("\n" + self.urxvtLine("color3", scheme, "yellow"))
        urxvtFile.write("\n" + self.urxvtLine("color11", scheme, "yellow2"))

        urxvtFile.write("\n!blue")
        urxvtFile.write("\n" + self.urxvtLine("color4", scheme, "blue"))
        urxvtFile.write("\n" + self.urxvtLine("color12", scheme, "blue2"))

        urxvtFile.write("\n!magenta")
        urxvtFile.write("\n" + self.urxvtLine("color5", scheme, "magenta"))
        urxvtFile.write("\n" + self.urxvtLine("color13", scheme, "magenta2"))

        urxvtFile.write("\n!cyan")
        urxvtFile.write("\n" + self.urxvtLine("color6", scheme, "cyan"))
        urxvtFile.write("\n" + self.urxvtLine("color14", scheme, "cyan2"))

        urxvtFile.write("\n!white")
        urxvtFile.write("\n" + self.urxvtLine("color6", scheme, "white"))
        urxvtFile.write("\n" + self.urxvtLine("color15", scheme, "white2"))

        urxvtFile.close()
