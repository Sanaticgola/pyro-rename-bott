"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
from helper.txt import mr
from helper.database import db
from helper.utils import not_subscribed 
from config import START_PIC, FLOOD, ADMIN 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="⭕𝙹𝚘𝚒𝚗 𝙼𝚢 𝙲𝚑𝚊𝚗𝚗𝚎𝚕⭕", url='https://t.me/Sanaticsmovies') ]]
    text = "**𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴 𝚈𝙾𝚄 HAVE 𝙽𝙾𝚃 𝙹𝙾𝙸𝙽E𝙳 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻. 𝙿𝙻𝙴𝙰𝚂𝙴 𝙹𝙾𝙸𝙽 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)    
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""HEY ROMEO 🌀{user.mention}
          <b> I AM A FAST RENAMER BOT WITH PERMANENT THUMBNAIL SUPPORT AND DOCUMENT TO VIDEO CONVERTOR BOT WITH CUSTOM CAPTION.""",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton('⭕ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ⭕', url='https://t.me/Sanaticsmovies')
           ],[
           InlineKeyboardButton('⭕ 𝙰𝙱𝙾𝚄𝚃 ⭕', callback_data='about'),
           InlineKeyboardButton('⭕ 𝙷𝙴𝙻𝙿 ⭕', callback_data='help')
           ]]
          )
       )
    return

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("✏ 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 ✏", callback_data="rename") ],
                   [ InlineKeyboardButton("❌ 𝙲𝙰𝙽𝙲𝙴𝙻 ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__WHAT YOU WANT ME TO DO WITH THIS FILE.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("✏ 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 ✏", callback_data="rename") ],
                   [ InlineKeyboardButton("❌ 𝙲𝙰𝙽𝙲𝙴𝙻 ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""HEY ROMEO 🌀{query.from_user.mention} 
            <b> I AM A FAST RENAMER BOT WITH PERMANENT THUMBNAIL SUPPORT AND VIDEO TO FILE CONVERTOR BOT WITH CUSTOM caption.""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton('⭕ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ⭕', url='https://t.me/Sanaticsmovies')
                ],[
                InlineKeyboardButton('⭕ 𝙰𝙱𝙾𝚄𝚃 ⭕', callback_data='about'),
                InlineKeyboardButton('⭕ 𝙷𝙴𝙻𝙿 ⭕', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=f"""Command list for sanatic bot
           <b> /start - bot alive cheking
           <b> /viewthumb - View Thumbnail
           <b> /delthumb - Delete Thumbnail
           <b> /set_caption - set a custom caption
           <b> /see_caption - see your custom caption
           <b> /del_caption - delete custom caption""",
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️#
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=f"""Since 2022 company
            <b> ✮ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/sridhar_814>SD</a>""",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("🖥️ 𝙷𝙾𝚆 𝚃𝙾 𝙼𝙰𝙺𝙴", url="https://youtu.be/GfulqsSnTv4")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





