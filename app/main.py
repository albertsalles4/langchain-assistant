from fastapi import FastAPI
from app.config import SERVER_HOST, SERVER_PORT, DEBUG
from telegram_handler import telegram_webhook
from twilio_handler import twilio_api_reply

# Create a FastAPI app instance
app = FastAPI()

# Include the routers for the Telegram webhook and Twilio API reply
app.include_router(telegram_webhook)
app.include_router(twilio_api_reply)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=SERVER_HOST, port=SERVER_PORT, reload=DEBUG)
