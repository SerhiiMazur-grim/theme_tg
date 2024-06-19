import os

from aiogram import Bot, loggers
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.types.user import User
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext

from app.keyboards.reply_kb.user_rkb import main_keyboard
from config.callback_data import (
    THEME_STEP_BACK,
    CANCEL_CREATE_THEME,
    AUTO_CREATE_THEME
)
from utils.theme import (
    CreateAndroidTheme,
    CreateComputerTheme,
    CreateIphoneTheme
)
from ..windows import CREATE_THEME_WINDOWS


class CreateThemeDialog(CreateAndroidTheme,
                        CreateComputerTheme,
                        CreateIphoneTheme):
    
    previous_window: str = THEME_STEP_BACK
    abort: str = CANCEL_CREATE_THEME
    auto_create_theme: str = AUTO_CREATE_THEME
    windows: dict = CREATE_THEME_WINDOWS
    
    def __init__(self, call: CallbackQuery, bot: Bot, state: FSMContext, i18n: I18nContext) -> None:
        self.call = call
        self.bot = bot
        self.state = state
        self.i18n = i18n
    
    
    @property
    def call_data(self):
        data: str = self.call.data
        return data
    
    
    async def state_data(self):
        data: dict = await self.state.get_data()
        return data
    
    
    async def step(self):
        data: dict = await self.state_data()
        return data.get('step')
    
    
    async def _step_back(self, step):
        step = step - 1
        data = await self.state.update_data(step=step)
        colors: list = data.get('color_list')
        window = self.windows.get(step)
        
        if step == 1:
            ikb = window.key_board(self.i18n)
        else:
            ikb = window.key_board(colors, self.i18n)
        
        return self.call.message.edit_caption(
            caption=window.caption(self.i18n),
            reply_markup=ikb
        )
    

    async def _clear_folder_and_state(self, chat_id):
        await self.state.clear()
        path = os.path.join('src', 'users_data', str(chat_id))
        if not os.path.exists(path):
            return
        
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            try:
                os.remove(file_path)
            except Exception as e:
                loggers.event.error(f'Failed to delete file {file} \n ERROR: {e}')


    async def _abort_create_theme(self):
        data = await self.state_data()
        chat_id = data.get('chat_id')
        await self._clear_folder_and_state(chat_id)
        await self.call.message.delete()
        await self.call.message.answer(text=self.i18n.messages.abort_create_theme(),
                                       reply_markup=main_keyboard(self.i18n))

    
    async def _create_theme(self, data):
        await self.call.message.delete()
        wait_message = await self.call.message.answer(self.i18n.messages.wait_creating_theme())
        bot_data: User = await self.bot.get_me()
        bot_username = bot_data.username
        device = data.get('device')
        chat_id = data.get('chat_id')
        
        try:
            # if device == 'android':
            #     theme_path, preview_path = await self.create_android_theme(data, bot_username)
            
            # elif device == 'iphone':
            #     theme_path, preview_path = await self.create_iphone_theme(data, bot_username)
            
            # elif device == 'computer':
            #     theme_path, preview_path = await self.create_pc_theme(data, bot_username)
            if device == 'android':
                theme_path = await self.create_android_theme(data, bot_username)
            
            elif device == 'iphone':
                theme_path = await self.create_iphone_theme(data, bot_username)
            
            elif device == 'computer':
                theme_path = await self.create_pc_theme(data, bot_username)
                
        except Exception as e:
            loggers.event.error(f'An error occurred while creating theme \n ERROR: {e}')
            await wait_message.delete()
            await self._clear_folder_and_state(chat_id)
            return self.call.message.answer(self.i18n.messages.error_creating_theme())
        
        await wait_message.delete()
        # await self.call.message.answer_photo(photo=FSInputFile(path=preview_path))
        await self.call.message.answer_document(document=FSInputFile(path=theme_path),
                                   caption=self.i18n.messages.your_theme_created(bot_username=bot_username),
                                   reply_markup=main_keyboard(self.i18n))
        
        await self._clear_folder_and_state(chat_id)
    
    
    async def _auto_create_theme(self):
        data: dict = await self.state_data()
        colors: list = data.get('color_list')
        device = data.get('device')
        
        if device == 'iphone':
            updated_data = await self.state.update_data({
                'bg_color': colors[0],
                'primary_color': colors[4],
                'secondary_color': colors[3]
            })
        else:
            updated_data = await self.state.update_data({
                'bg_color': colors[0],
                'primary_color': colors[4],
                'secondary_color': colors[3],
                'alfa_chanel': 'e6'
            })
        theme = await self._create_theme(updated_data)
        
        return theme
    
    
    async def _step_1(self):
        data: dict = await self.state_data()
        colors: list = data.get('color_list')
        step: int = int(await self.step()) + 1
        window = self.windows.get(step)
        await self.state.update_data({
            'step': step,
            'device': self.call_data})
        
        return self.call.message.edit_caption(
            caption=window.caption(self.i18n),
            reply_markup=window.key_board(colors, self.i18n)
        )
    
    
    async def _step_2(self):
        data: dict = await self.state_data()
        colors: list = data.get('color_list')
        step: int = int(await self.step()) + 1
        window = self.windows.get(step)
        await self.state.update_data({
            'step': step,
            'bg_color': self.call_data
        })
        
        return self.call.message.edit_caption(
            caption=window.caption(self.i18n),
            reply_markup=window.key_board(colors, self.i18n)
        )
    
    
    async def _step_3(self):
        data: dict = await self.state_data()
        bg_color = data.get('bg_color')
        if bg_color == self.call_data:
            return await self.call.answer(text=self.i18n.messages.error_same_color(),
                                    show_alert=True)
        
        colors: list = data.get('color_list')
        step: int = int(await self.step()) + 1
        window = self.windows.get(step)
        await self.state.update_data({
            'step': step,
            'primary_color': self.call_data
        })
        
        return self.call.message.edit_caption(
            caption=window.caption(self.i18n),
            reply_markup=window.key_board(colors, self.i18n)
        )
    
    
    async def _step_4(self):
        data: dict = await self.state_data()
        bg_color = data.get('bg_color')
        if bg_color == self.call_data:
            return await self.call.answer(text=self.i18n.messages.error_same_color(),
                                    show_alert=True)
        
        step: int = int(await self.step()) + 1
        window = self.windows.get(step)
        data: dict = await self.state.update_data({
            'step': step,
            'secondary_color': self.call_data
        })
        device = data.get('device')
        
        if device == 'iphone':
            theme = await self._create_theme(data)
            return theme
        
        return self.call.message.edit_caption(
            caption=window.caption(self.i18n),
            reply_markup=window.key_board(self.i18n)
        )
    
    
    async def _step_5(self):
        data = await self.state.update_data(alfa_chanel=self.call_data)        
        theme = await self._create_theme(data)
        
        return theme
    
    
    async def step_processing(self):
        step: int = int(await self.step())
        
        if self.call_data == self.previous_window:
            return await self._step_back(step)
        
        elif self.call_data == self.abort:
            return await self._abort_create_theme()
        
        elif self.call_data == self.auto_create_theme:
            return await self._auto_create_theme()
        
        if step == 1:
            return await self._step_1()
        elif step == 2:
            return await self._step_2()
        elif step == 3:
            return await self._step_3()
        elif step == 4:
            return await self._step_4()
        elif step == 5:
            return await self._step_5()
