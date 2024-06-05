from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.types.user import User
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext

from config.callback_data import THEME_STEP_BACK
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
    windows: dict = CREATE_THEME_WINDOWS
    
    def __init__(self, call: CallbackQuery, bot: Bot, state: FSMContext, i18n: I18nContext) -> None:
        self.call = call
        self.bot = bot
        self.state = state
        self.i18n = i18n
    
    
    @property
    def call_data(self):
        data: str = self.call.data
        if data==self.previous_window:
            return data
        return data.split('_')[-1]
    
    
    async def state_data(self):
        data: dict = await self.state.get_data()
        return data
    
    
    async def step(self):
        data: dict = await self.state_data()
        return data.get('step')
    
    
    # step_back = call.data == 'step_back'
    # if step_back:
    #     data = await state.get_data()
    #     step = data.get('step')-1
    #     color_list = data.get('color_list')
    #     window = windows.get(step)
    #     await state.update_data(step=step)
    #     return call.message.edit_caption(
    #         caption=window.caption(i18n),
    #         reply_markup=window.key_board(color_list)
    #     )
    
    
    async def _create_theme(self, data):
        await self.call.message.delete()
        bot_data: User = await self.bot.get_me()
        bot_username = bot_data.username
        photo_message: Message = data.get('photo_message')
        device = data.get('device')
        if device == 'android':
            theme_path = await self.create_android_theme(data, bot_username)
        
        elif device == 'iphone':
            theme_path = await self.create_iphone_theme(data, bot_username)
        
        elif device == 'computer':
            theme_path = await self.create_pc_theme(data, bot_username)
        
        return photo_message.reply_document(document=FSInputFile(path=theme_path),
                                            caption=f'Ваша тема для {device} готова')
    
    
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
            return self.call.message.answer('we back to previous window')
        elif step == 1:
            return await self._step_1()
        elif step == 2:
            return await self._step_2()
        elif step == 3:
            return await self._step_3()
        elif step == 4:
            return await self._step_4()
        elif step == 5:
            return await self._step_5()
        
    