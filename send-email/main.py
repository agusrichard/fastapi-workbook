import uvicorn
from fastapi import FastAPI, BackgroundTasks
from send_email import send_email_background, send_email_async

app = FastAPI()


@app.get('/')
def index():
    return 'Hello World'


@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async('Hello World', 'richardagus921@gmail.com', {
        'name': 'Hello World'
    })
    return 'Success'


@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'Hello World', 'richardagus921@gmail.com', {
        'name': 'Hello World'
    })
    return 'Success'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
