import os

from PIL import Image, ImageDraw, ImageFont

from config import water_mark_text
from .hex_to_rgba_convert import HexColorToRgba
from .crop_wallpaper import CropWallpaper
from .android_theme_layers.android_loaded_layers import ANDROID_USER_ICON_LIST, get_android_layers


class CreateAndroidPreview(HexColorToRgba, CropWallpaper):     
    
    async def _colored_android_users_icons(self, colors):
        painted_icons = []
        images = ANDROID_USER_ICON_LIST.copy()
        fill_start_y = 269
        fill_end_y = 343

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
            fill_start_y += 94
            fill_end_y += 94
            painted_icons.append(new_img)
        
        return painted_icons
    
    
    async def _colored_android_layers(self, images, colors):
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
    
    
    async def create_android_preview(self, bot_username, chat_id, photo, alfa, bg, primary_txt, secondary_txt, chat_in,
                           avatar_gradient1, avatar_gradient2, preview_bg):
        watermark = water_mark_text(bot_username)
        background = Image.new('RGB', (1088, 1088), 'white')

        layers = []
        wallpaper = await self._crop_wallpaper(photo)
        images = await get_android_layers()
        
        colors = await self._hex_color_to_rgba([
            preview_bg,
            bg,
            bg+alfa,
            chat_in+alfa,
            primary_txt,
            secondary_txt,
            avatar_gradient2
        ])

        
        assets = await self._colored_android_layers(images, colors)
        layers.extend(i for i in assets)
        
        icons = await self._colored_android_users_icons(await self._hex_color_to_rgba([avatar_gradient1, avatar_gradient2]))
        layers.extend(i for i in icons)
        
        background.paste(wallpaper, (45, 155))
        
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
    