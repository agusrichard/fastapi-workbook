import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Conductor Orchestraion Main')


@app.get('/')
def root():
    return 'Conductor Orchestraion Main'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
