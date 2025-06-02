from fastapi import FastAPI

app = FastAPI(title="EduConecta Bot Backend")

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "ok", "message": "EduConecta Bot is running!"}