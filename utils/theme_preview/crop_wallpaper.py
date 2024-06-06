from PIL import Image


class CropWallpaper():
    
    async def _crop_wallpaper(self, wallpaper_path):
        with Image.open(wallpaper_path) as img:
            width, height = img.size
            
            if width > int(height*0.7):
                top_x = width//2 - int(height*0.7)//2
                top_y = 0
                bot_x = width//2 + int(height*0.7)//2
                bot_y = height
                
            else:
                top_x = 0
                top_y = height//2 - int(width//0.7)//2
                bot_x = width
                bot_y = height//2 + int(width//0.7)//2

            cropped_img = img.crop((top_x, top_y, bot_x, bot_y))
        new_width = int((750 / cropped_img.size[1]) * cropped_img.size[0])
        wallpaper = cropped_img.resize((new_width, 750))
        
        return wallpaper
    
    
    async def _crop_computer_wallpaper(self, wallpaper_path):
        with Image.open(wallpaper_path) as img:
            width, height = img.size
            
            if width > height:
                top_x = width//2 - height//2
                top_y = 0
                bot_x = width//2 + height//2
                bot_y = height
                
            else:
                top_x = 0
                top_y = height//2 - width//2
                bot_x = width
                bot_y = height//2 + width//2

            cropped_img = img.crop((top_x, top_y, bot_x, bot_y))
        wallpaper = cropped_img.resize((535, 555))
        
        return wallpaper
