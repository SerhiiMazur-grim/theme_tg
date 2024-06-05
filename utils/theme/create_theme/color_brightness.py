
class ColorBrightness():
    
    async def _adjust_color_brightness(self, hex_color, factor=0.1):
        color = int(hex_color[1:], 16)

        red = (color >> 16) & 0xFF
        green = (color >> 8) & 0xFF
        blue = color & 0xFF

        brightness = (red + green + blue) / 3.0

        if brightness < 128:
            new_red = int(red + (255 - red) * factor)
            new_green = int(green + (255 - green) * factor)
            new_blue = int(blue + (255 - blue) * factor)
        else:
            new_red = int(red * (1 - factor))
            new_green = int(green * (1 - factor))
            new_blue = int(blue * (1 - factor))

        new_red = max(0, min(255, new_red))
        new_green = max(0, min(255, new_green))
        new_blue = max(0, min(255, new_blue))

        new_color = "#{:02X}{:02X}{:02X}".format(new_red, new_green, new_blue)
        
        return new_color