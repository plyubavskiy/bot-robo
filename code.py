import telebot, wikipedia, re


bot = telebot.TeleBot('TOKEN')


wikipedia.set_lang('ru')

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'У этого значения есть слишком много определений. \nПопробуй уточнить фразой или обратись за помощью Google.com'



@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, '\nПривет, {0.first_name}! \nЯ - бот, который поможет тебе узнать инфо о твоем запросе 😏'
                                '\n\nЧтож приступим! Вводи слова или фразы, когда закончишь - не забудь меня остановить и блокировать!'
                                '\n\nУдачи {0.first_name} 😁!'.format(m.from_user))

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)
