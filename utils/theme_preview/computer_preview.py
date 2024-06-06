import os

from PIL import Image, ImageDraw, ImageFont

from config import water_mark_text
from .hex_to_rgba_convert import HexColorToRgba
from .crop_wallpaper import CropWallpaper
from .pc_theme_layers.computer_loaded_layers import PC_USER_ICON_LIST, PC_IMAGE_LAYER_LIST


class CreateComputerPreview(HexColorToRgba, CropWallpaper):
    
    async def _colored_computer_users_icons(self, colors):
        painted_icons = []
        images = PC_USER_ICON_LIST.copy()
        fill_start_y = 335
        fill_end_y = 398

        for image in images:
            width, _ = image['size']
            new_img = Image.new("RGBA", image['size'])
            alpha_channel = image['alpha']
                
            gradient_start_color = colors[0]
            gradient_end_color = colors[1]

            draw = ImageDraw.Draw(new_img)

            for y in range(fill_start_y, fill_end_y):
                t = (y - fill_start_y) / (fill_end_y - fill_start_y)
                r = int((1 - t) * gradient_start_color[0] + t * gradient_end_color[0])
                g = int((1 - t) * gradient_start_color[1] + t * gradient_end_color[1])
                b = int((1 - t) * gradient_start_color[2] + t * gradient_end_color[2])
                
                intermediate_color = (r, g, b)
                
                draw.line([(0, y), (width, y)], fill=intermediate_color)

            new_img.putalpha(alpha_channel)
            fill_start_y += 80
            fill_end_y += 80
            painted_icons.append(new_img)
            
        return painted_icons
    
    
    async def _colored_computer_layers(self, images, colors):
        layers = []
        for image, color in zip(images, colors):
            img_data = image['img_data']
            alpha_channel = image['alpha']

            if len(color) == 4:
                new_img_data = [
                    (color[0], color[1], color[2],  color[3]) if alpha > 0 else pixel
                    for pixel, alpha in zip(img_data, alpha_channel)
                ]
            else:
                new_img_data = [
                (color[0], color[1], color[2],  alpha) if alpha > 0 else pixel
                for pixel, alpha in zip(img_data, alpha_channel)
                ]

            new_img = Image.new("RGBA", image['size'])
            new_img.putdata([tuple(p) for p in new_img_data])
            layers.append(new_img)

        return layers
    
    
    async def create_pc_preview(self, bot_username, chat_id, photo, img_bg_color, chat_bg, clouds_in_color, 
                              secondary_txt_color, prime_txt_color, alfa):
        watermark = water_mark_text(bot_username)
        background = Image.new('RGB', (1088, 1088), 'white')

        layers = []
        wallpaper = await self._crop_computer_wallpaper(photo)
        images = PC_IMAGE_LAYER_LIST.copy()
        
        colors = await self._hex_color_to_rgba([
            img_bg_color,
            chat_bg,
            clouds_in_color,
            secondary_txt_color,
            clouds_in_color+alfa,
            chat_bg+alfa,
            prime_txt_color,
            secondary_txt_color,
            secondary_txt_color,
        ])

        
        assets = await self._colored_computer_layers(images, colors)
        layers.extend(i for i in assets)
        
        icons = await self._colored_computer_users_icons(await self._hex_color_to_rgba([chat_bg, secondary_txt_color]))
        layers.extend(i for i in icons)
        
        background.paste(wallpaper, (511, 304))
        
        for layer in layers:
            background.paste(layer, (0, 0), layer)
        
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("arial.ttf", 20)
        text_color = colors[1]
        position = (40, 1025)

        draw.text(position, watermark, font=font, fill=text_color)
        
        preview = os.path.join('src', 'users_data', str(chat_id), 'preview.jpg')
        
        background.save(preview)
        
        return preview
