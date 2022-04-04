#!/usr/bin/python3.8
#garpozir@gmail.com
#baba-god

from telegram.ext import(
        Updater,
        CommandHandler,
        MessageHandler,
        Filters,
        ConversationHandler,
        CallbackContext,
        CallbackQueryHandler
)
import telegram,time,hashlib,sqlite3,datetime,os
from telegram import Update,ForceReply,Sticker,KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
import json
import logging
from telegram import Update, ForceReply

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
tar,voice,end=range(3)
bol=False

def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('عملیات لغو شد')
    return ConversationHandler.END

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        #reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('/start راه اندازی ربات\n\n/help راهنما\n\n/report گزارش از تراکنش کاربران\n\n/credit ویرایش موجودی کاربران')

def echo(update: Update, context: CallbackContext) -> None:
    if update.message.text=='/See_details':
        with open('./details','r') as fd:
            jsn=fd.read()
            fd.close()
        update.message.reply_text(jsn)
    else:
    #update.message.reply_text(update.message.text)
        update.message.reply_text('چنین دستوری وجود ندارد')

def credit(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('کلمه عبور و جی‌میل مورد نظر را با فرمت زیر وارد کنید'+'\npassword+example@gmail.com')
    return voice

def TAR(update: Update, context: CallbackContext) -> None:
    tedad_se=update.message.text
    if tedad_se.isdigit() and int(tedad_se)<10000001:
        with open('../public/contact.json','r') as fd:
            jsn=json.load(fd)
            fd.close()
        jsn['member'][gmail1]=int(tedad_se)
        with open('../public/contact.json','w') as fd:
            json.dump(jsn,fd)
            fd.close()
        update.message.reply_text('👍با موفقیت انجام شد')
        with open('../public/contact.json','r') as fd:
            jsn=json.load(fd)
            fd.close()
        update.message.reply_text('تعداد سکه های فعلی'+'\n'+gmail1+'\n'+str(jsn['member'][gmail1]))
        return ConversationHandler.END
    else:
        update.message.reply_text('لطفا یک عدد حداکثر تا ده میلیون سکه وارد کنید')

def END(update: Update, context: CallbackContext) -> None:
    reply_keyboard = ['👍ویرایش','👍نمایش']
    if update.message.text in reply_keyboard and bol==True:
        if update.message.text==reply_keyboard[0]:
            update.message.reply_text('تعداد سکه های کاربر را وارد کنید',reply_markup=telegram.ReplyKeyboardRemove())
            return tar
        elif update.message.text==reply_keyboard[1]:
            update.message.reply_text('تعداد سکه های کاربر:  '+str(gmail),reply_markup=telegram.ReplyKeyboardRemove())
            return ConversationHandler.END
    else:
        update.message.reply_text('یکی از گزینه ها را انتخاب کنید')
        #update.message.reply_text('یکی از گزینه ها را انتخاب کنید',reply_markup=telegram.ReplyKeyboardRemove())

def VOICE(update: Update, context: CallbackContext) -> None:
    try:
        pas=(update.message.text).find('+')
        with open('../public/contact.json','r') as fd:
            jsn=json.load(fd)
            fd.close()
        global gmail
        global gmail1
        try:
            gmail=jsn['member'][(update.message.text).split('+')[1]]
            gmail1=(update.message.text).split('+')[1]
        except:pass
        if(update.message.text).split('+')[1] in jsn['member'].keys() and pas!=-1 and (update.message.text).split('+')[0]=='oliver_4669':
            global bol
            bol=True
            reply_keyboard = [['👍ویرایش','👍نمایش']]
            update.message.reply_text('یکی از گزینه ها را انتخاب کنید',                                         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True,input_field_placeholder=''))
            return end
        else:
            update.message.reply_text('خطا. کلمه عبور یا جی‌میل اشتباه است')
#            return ConversationHandler.END
    except:
        update.message.reply_text('خطایی رخ داد. دوباره تلاش کنید.')
        return ConversationHandler.END

def report(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text('repiiiiiii')
    sood=10
    with open('../public/contact.json','r') as fd:
        jsn=json.load(fd)
        fd.close()
    usr_count=len(jsn['member'].keys())
    game_count=len(jsn['level'].keys())
    key=jsn['level'].keys()
    lst=list(map(lambda x:int(x.split('**')[1]),jsn['level'].keys()))
    sood_site=sum(lst)
    sum_all_games=sum(lst)*sood
    sood_usr=sum_all_games-sood_site
    balatarin=max(lst)*sood
    str_match = [s for s in key if str(max(lst)) in s]
    tarick_balatarin=jsn['level'][str_match[0]]

    txt = '{pr:,}'
    usr_count=txt.format(pr=usr_count)
    game_count=txt.format(pr=game_count)
    sum_all_games=txt.format(pr=sum_all_games)
    sood_usr=txt.format(pr=sood_usr)
    sood_site=txt.format(pr=sood_site)
    balatarin=txt.format(pr=balatarin)

    update.message.reply_text('تعداد کل کاربران: '+str(usr_count)+' نفر '+'\n'+'تعداد کل بازیها: '+str(game_count)+' بازی '+'\n'+'مجموع تمام تراکنشها: '+str(sum_all_games)+' سکه '+'\n'+'کل عایدی کاربران: '+str(sood_usr)+' سکه '+'\n'+'کل عایدی سایت: '+str(sood_site)+' سکه '+'\n'+'رکوردار بالاترین تراکنش: '+str(balatarin)+' سکه به تاریخ '+tarick_balatarin+'\n\n'+'ریز تراکنشها را در لینک زیر مشاهده کنید'+'\n'+'/See_details')

    with open('./details','w') as fd:
        cnt_new=0
        for i in key:
            tarick=jsn['level'][i]
            sood_site_one=lst[cnt_new]
            poole_bazi_one=lst[cnt_new]*sood
            sood_usr_one=poole_bazi_one-lst[cnt_new]
            txt = '{pr:,}'
            poole_bazi_one=txt.format(pr=poole_bazi_one)
            sood_usr_one=txt.format(pr=sood_usr_one)
            sood_site_one=txt.format(pr=sood_site_one)
            fd.write('تاریخ تراکنش: '+tarick+'\n')
            fd.write('تعداد کل سکه های بازی: '+poole_bazi_one+'\n')
            fd.write('سهم کاربر برنده از سکه ها: '+sood_usr_one+'\n')
            fd.write('سهم سایت از سکه ها: '+sood_site_one+'\n')
            fd.write('**************\n')
            cnt_new+=1
    fd.close()

def main() -> None:
    """Start the bot."""
    updater = Updater("5126575062:AAGIIdiZftf1DbC26iaM53zLaWbZ4yXYe_s")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("report", report))
    #dispatcher.add_handler(CommandHandler("credit", credit))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('credit', credit)],
        states={
            voice: [MessageHandler(Filters.all, VOICE)],
            end: [MessageHandler(Filters.all, END)],
            tar: [MessageHandler(Filters.all, TAR)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
