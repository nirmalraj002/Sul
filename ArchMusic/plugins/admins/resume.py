#
# Copyright (C) 2021-2023 by ArchBots@Github, < https://github.com/ArchBots >.
#
# This file is part of < https://github.com/ArchBots/ArchMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ArchBots/ArchMusic/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from ArchMusic import app
from ArchMusic.core.call import ArchMusic
from ArchMusic.utils.database import is_music_playing, music_on
from ArchMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await ArchMusic.resume_stream(chat_id)
    photo_url = "https://telegra.ph/file/d5c7d064c59486614c703.jpg"  # Replace with the URL of the photo you want to send
    await message.reply_photo(
        photo=photo_url        
    )
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention)
    )
