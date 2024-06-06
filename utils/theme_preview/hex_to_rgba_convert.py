class HexColorToRgba():
    async def _hex_color_to_rgba(self, hex_colors):
        rgb_colors = []
        for hex_color in hex_colors:
            hex_color = hex_color.lstrip('#')

            if len(hex_color) == 6:
                rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
                rgb_colors.append(rgb)
            elif len(hex_color) == 8:
                rgba = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4, 6))
                rgb_colors.append(rgba)
        
        return rgb_colors
    