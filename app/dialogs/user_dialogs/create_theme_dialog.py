from dataclasses import dataclass

from aiogram.types import InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext

from app.keyboards.inline_kb.user_ikb import (
    choose_color_ikb,
    choose_alfa_ikb
)


@dataclass
class Window:
    message_key: str
    key_board: InlineKeyboardMarkup
    
    def caption(self, i18n: I18nContext) -> str:
        locale: str = i18n.locale
        return i18n.core.get(self.message_key, locale) 
        


CREATE_THEME_WINDOWS = [
    Window(
        message_key = 'messages-choose_main_coloro_bg',
        key_board = choose_color_ikb
    ),
    Window(
        message_key = 'messages-choose_main_color_text',
        key_board=choose_alfa_ikb
    )
]


class CreateThemeDialog():
    previous_window: str = 'previous_window'
    windows: list = CREATE_THEME_WINDOWS
    
    def __init__(self, call: CallbackQuery, state: FSMContext, i18n: I18nContext) -> None:
        self.call = call
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
    #     window = windows[step]
    #     await state.update_data(step=step)
    #     return call.message.edit_caption(
    #         caption=window.caption(i18n),
    #         reply_markup=window.key_board(color_list)
    #     )
    
    
    async def _step_0(self):
        step: int = int(await self.step()) + 1
        window = self.windows[step]
        await self.state.update_data(bg_color=self.call_data)
        await self.state.update_data(step=step)
        
        return self.call.message.edit_caption(
            caption=window.caption(self.i18n),
            reply_markup=window.key_board()
        )
    
    
    async def _step_1(self):
        await self.state.update_data(alfa_chanel=self.call_data)
        data: dict = await self.state_data()
        await self.state.clear()
        await self.call.message.delete()
        return self.call.message.answer(text='тема готова')
    
    
    async def step_processing(self):
        step: int = int(await self.step())
        if self.call_data == self.previous_window:
            return self.call.message.answer('we back to previous window')
        elif step == 0:
            return await self._step_0()
        elif step == 1:
            return await self._step_1()
        
    