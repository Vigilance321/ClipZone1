from database import USERS_FILE, load_data, save_data

def register():
    print("\n--- Регистрация ---")
    username = input("Придумайте логин: ").strip()
    password = input("Придумайте пароль: ").strip()

    if not username or not password:
        print("Логин и пароль не должны быть пустыми.")
        return

    users = load_data(USERS_FILE)

    if any(user["username"].lower() == username.lower() for user in users):
        print("Такой пользователь уже существует.")
        return

    users.append({
        "username": username,
        "password": password,
        "bio": "Новый пользователь ClipZone"
    })
    save_data(USERS_FILE, users)
    print("Регистрация успешно завершена.")

def login():
    print("\n--- Вход ---")
    username = input("Логин: ").strip()
    password = input("Пароль: ").strip()

    users = load_data(USERS_FILE)

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Добро пожаловать, {username}!")
            return username

    print("Неверный логин или пароль.")
    return None
