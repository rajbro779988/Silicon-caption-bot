import os

class script(object):

    START_TXT = """<b>Hᴇʟʟᴏ {} 👋\n\n
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ cʜᴀɴɴᴇʟ ᴀɴᴅ ᴇɴᴊᴏʏ

‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/SB_Botz_Update'>ꜱʙ ʙᴏᴛᴢ ᴜᴘᴅᴀᴛᴇ 🤞</a></b>
"""

    HELP_TXT = """•••[( 𝘎𝘦𝘵 𝘏𝘦𝘭𝘱 )]•••

❗ 𝗔𝗹𝗲𝗿𝘁 ❗

• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.

•> /set_cap - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
•> /del_cap - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ

𝑭𝒐𝒓𝒎𝒂𝒕

`{file_name}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Nᴀᴍᴇ
`{file_size}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Sɪᴢᴇ 
`{language}` = Lᴀɴɢᴜᴀɢᴇ Oғ Fɪʟᴇ
`{quality}` = Qᴜᴀʟɪᴛʏ ᴏғ ғɪʟᴇ
`{file_type}` = Tʏᴘᴇ ᴏғ ғɪʟᴇ
`{year}` = Yᴇᴀʀ Oғ Fɪʟᴇ
`{default_caption}` = Rᴇᴀʟ Cᴀᴘᴛɪᴏɴ Oғ Fɪʟᴇ.

Eg:- `/set_cap
{file_name}

⚙️ Size » {file_size}

╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ 
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝`
"""

    ABOUT_TXT = """<b>╔════❰ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : <a href='https://t.me/SbAutoCaptionBot'>𝘼𝙪𝙩𝙤 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 𝙗𝙤𝙩</a>
║┣⪼👦Bᴏᴛ Oᴡɴᴇʀ : <a href='https://t.me/Your_RJV'>𝚁𝚊𝚓 𝚅𝚎𝚛𝚖𝚊 ⚝</a>
║┣⪼🤖Uᴘᴅᴀᴛᴇ : <a href='https://t.me/Sb_botz_Update'>ꜱʙ ʙᴏᴛᴢ ᴜᴘᴅᴀᴛᴇ™</a>
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ 
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
║┣⪼📚Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ 2.11.6
║┣⪼🗒️Vᴇʀsɪᴏɴ : 2.0.8 [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""
