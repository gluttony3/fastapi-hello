from fastapi import FastAPI, HTTPException

app = FastAPI()
user = []

# ендопоінт для списка всіх юзерів
@app.get("/users/get-all")
def get_all_users():
    return{"all_users: users"}

@app.get("/user/{login}")
def get_user(login):
    for user in users:
        if user ["login"] == login:
            return user
            raise HTTPException(status_code=404, detail="User not found")

# ендпоінт для додавання юзера
@app.post("/user/add")
def add_user(login: str,first_name: str,last_name: str,birth_year: int):
    new_user = {
        "login" : login,
        "first_name": first_name,
        "last_name" : last_name,
        "birth_year": birth_year
    }
    users.append(new_user)
    return{"message": "user was added succesfully","new_user": new_user}
# ендпоінт для видалення юзера 
@app.delete("/user/delete/{login}")
def user_delete(login):
    for user in users:
        if user[login] == login:
            user.remove(user)
            return {"message": "User was delete succesfully"}
            raise HTTPException(status_code=404, detail="User not found")
# ендпошнт для повного оновлення юзера
@app.put("/delete/update/")
def full_update(login: str , new_name: str , new_surname: str, new_birth_year: int):
    for user in users:
        if user["login"] == login:
            user["first_name"] = new_name,
            user["last_name"] = new_surname,
            user["birth_year"] = new_birth_year,

            return {"message": "User updated succesfully","user": user}
    raise HTTPException(status_code=404,detail="User not found")











#get - отримати
#post - створити 
#put - повне оновлення
#patch - часткове оновлення
#delete - відправити запит на видалення