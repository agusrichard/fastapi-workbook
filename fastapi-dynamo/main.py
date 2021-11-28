"""
Pylint told me to write in here
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    """
    Pylint told me to write in here
    """
    return 'Hello World'


if __name__ == '__main__':
    uvicorn.run('main:app')
