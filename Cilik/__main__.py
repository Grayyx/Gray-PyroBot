# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Cilik-PyroBot

from pyrogram import idle
from uvloop import install

from config import BOT_VER
from Cilik import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from Cilik.helpers.misc import create_botlog, git, heroku

MSG_ON = """
✅ **Gray-PyroBot Activated.**
**🏷️ Userbot Version -** `{}`
**Ketik** `.gray` **untuk Mengecheck Bot**
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("CilikProject")
            await bot.join_chat("CilikSupport")
            await bot.join_chat("GrayStoreee1")
            await bot.join_chat("Graymemberr")
            await bot.join_chat("SharingUserbot")            
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER)
                )
            except BaseException:
                pass
            LOGGER("Gray").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Gray").info(f"Gray-PyroBot v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Gray").info("Starting Gray-PyroBot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
