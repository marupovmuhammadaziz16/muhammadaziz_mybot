from aiogram import Router, types
rt = Router()
@rt.message()
async def info(msg: types.Message):
    await msg.answer(str(msg.text))