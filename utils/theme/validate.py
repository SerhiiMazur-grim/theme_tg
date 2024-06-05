from aiogram.types import Message


def is_photo_id(message: Message) -> bool | str:
    if message.photo:
        photo = message.photo[-1].file_id
        return photo
    
    if message.document:
        if message.document.mime_type != 'image/jpeg':
            return False
        else:
            photo = message.document.file_id
            return photo
        
    return False