from database import USERS_FILE, VIDEOS_FILE, load_data

def show_profile(username):
    users = load_data(USERS_FILE)
    videos = load_data(VIDEOS_FILE)

    user = next((u for u in users if u["username"] == username), None)
    if not user:
        print("Пользователь не найден.")
        return

    user_videos = [v for v in videos if v["author"] == username]
    total_likes = sum(v["likes"] for v in user_videos)
    total_views = sum(v["views"] for v in user_videos)

    print("\n--- Профиль ---")
    print(f"Логин: {user['username']}")
    print(f"Описание: {user['bio']}")
    print(f"Видео: {len(user_videos)}")
    print(f"Лайков: {total_likes}")
    print(f"Просмотров: {total_views}")
