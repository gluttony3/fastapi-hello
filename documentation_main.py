from fastapi import FastAPI
# Створення екземпляру FastAPI
app = FastAPI()
# Маршрут, який обробляє GET-запити на кореневий шлях
"/"
@app.get("/")
def index():
 return "Hello FastAPI!"