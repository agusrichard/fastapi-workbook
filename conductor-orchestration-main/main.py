import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Conductor Orchestraion Main')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {"message": "Sekardayu Hana Pradiani", "success": True}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=8081)
