import webcolors


class ColorName():
    async def get_closest_color_name(self, hex_value):
        min_colors = {}
        for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            r, g, b = webcolors.hex_to_rgb(hex_value)
            rd = (r_c - r) ** 2
            gd = (g_c - g) ** 2
            bd = (b_c - b) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]
    
    
    async def hex_to_color_name(self, hex_value):
        try:
            color_name = webcolors.hex_to_name(hex_value)
        except ValueError:
            closest_name = await self.get_closest_color_name(hex_value)
            return closest_name
        return color_name