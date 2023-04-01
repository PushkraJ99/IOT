from telegram import Update
from telegram.ext import*
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

async def  hello(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"HEY THERE...")
    
async def  turnOn(update:Update,context:ContextTypes.DEFAULT_TYPE):
    GPIO.output(3,GPIO.HIGH)
    await update.message.reply_text(f"LED ON")
    
async def  turnOff(update:Update,context:ContextTypes.DEFAULT_TYPE):
    GPIO.output(3,GPIO.LOW)
    await update.message.reply_text(f"LED off")
      

    
    
app=ApplicationBuilder().token("Enter Telegram Bot Token").build()
app.add_handler(CommandHandler("on",turnOn))
app.add_handler(CommandHandler("off",turnOff))
app.add_handler(CommandHandler("start",hello))

app.run_polling()