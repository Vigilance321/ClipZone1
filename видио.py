from database import VIDEOS_FILE, load_data, save_data

def next_video_id(videos):
    return max((video["id"] for video in videos), default=0) + 1

def add_video(username):
    print("\n--- Добавление видео ---")
    title = input("Название: ").strip()
    description = input("Описание: ").strip()

    if not title:
        print("Название не может быть пустым.")
        return

    videos = load_data(VIDEOS_FILE)
    video = {
        "id": next_video_id(videos),
        "title": title,
        "description": description,
        "author": username,
        "views": 0,
        "likes": 0,
        "liked_by": []
    }
    videos.append(video)
    save_data(VIDEOS_FILE, videos)
    print(f"Видео добавлено. Его ID: {video['id']}")

def list_videos(author=None):
    videos = load_data(VIDEOS_FILE)

    if author:
        videos = [v for v in videos if v["author"] == author]

    print("\n========== ЛЕНТА ==========")

    if not videos:
        print("Видео пока нет.")
        return

    for video in videos:
        print(f"\n[{video['id']}] {video['title']}")
        print(f"Автор: {video['author']}")
        print(f"❤️ {video['likes']}    👁 {video['views']}")
        print(f"Описание: {video['description']}")

def like_video(video_id, username):
    try:
        video_id = int(video_id)
    except ValueError:
        print("ID должен быть числом.")
        return

    videos = load_data(VIDEOS_FILE)

    for video in videos:
        if video["id"] == video_id:
            if username in video["liked_by"]:
                video["liked_by"].remove(username)
                video["likes"] -= 1
                print("Лайк убран.")
            else:
                video["liked_by"].append(username)
                video["likes"] += 1
                print("Лайк поставлен.")
            save_data(VIDEOS_FILE, videos)
            return

    print("Видео не найдено.")

def delete_video(video_id, username):
    try:
        video_id = int(video_id)
    except ValueError:
        print("ID должен быть числом.")
        return

    videos = load_data(VIDEOS_FILE)

    for video in videos:
        if video["id"] == video_id:
            if video["author"] != username:
                print("Можно удалять только свои видео.")
                return
            videos.remove(video)
            save_data(VIDEOS_FILE, videos)
            print("Видео удалено.")
            return

    print("Видео не найдено.")

def search_videos():
    query = input("Введите название или описание для поиска: ").strip().lower()
    videos = load_data(VIDEOS_FILE)

    results = [
        v for v in videos
        if query in v["title"].lower() or query in v["description"].lower()
    ]

    print("\n--- Результаты поиска ---")
    if not results:
        print("Ничего не найдено.")
        return

    for video in results:
        print(f"[{video['id']}] {video['title']} — {video['author']}")
