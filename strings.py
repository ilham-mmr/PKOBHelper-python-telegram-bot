START_MSG = '''
Hello {}, I am PKOB bot. please choose an option:
'''

START_ECHO_MSG = '''
Hello again {}, I am PKOB bot. please choose an option:
'''

GET_VICTIM_MSG = '''
Hello {}, Please input your ic and phone number with the following format:
    🟢 ic#phone 
    example:
    ✅ 123456123456#012341234
'''

GET_HELP_MSG = '''
            if you find any issues, kindly contact admin on 08123123123
        '''
WEBISTE_MSG = '''
our website : https://pkob268954.herokuapp.com/
'''

ABOUT_GENERAL_MSG = '''
{}, You seem curious. What do you want to know?
'''

ABOUT_DEVELOPER_MSG = '''
The bot created by ilham (268954).
checkout his github: https://github.com/ilham-mmr
'''

ABOUT_BOT_MSG = '''
The bot's objective is to help victims check their assistance status.
The bot is made using python-telegram-bot library connected to the main resource through API with Django.
'''

VICTIM_INFO_MSG = '''
<b>Victim's Information</b>\n
<b> Kad Pengenalan: {} </b>
<b> Nombor Telefon: {} </b>
<b> Nama: {} </b>
<b> Umur: {} </b>
'''

# 12 digits of ic #phone number
VICTIM_INFO_REGEX = r'^[0-9]{12}#[0-9]*$'
