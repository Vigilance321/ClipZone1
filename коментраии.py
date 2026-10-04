from database import COMMENTS_FILE, load_data, save_data

def add_comment(video_id, username):
    text = input("Введите комментарий: ").strip()
    if not text:
        print("Комментарий не может быть пустым.")
        return

    try:
        video_id = int(video_id)
    except ValueError:
        print("ID должен быть числом.")
        return

    comments = load_data(COMMENTS_FILE)
    comments.append({
        "video_id": video_id,
        "author": username,
        "text": text
    })
    save_data(COMMENTS_FILE, comments)
    print("Комментарий добавлен.")

def show_comments(video_id):
    try:
        video_id = int(video_id)
    except ValueError:
        print("ID должен быть числом.")
        return

    comments = load_data(COMMENTS_FILE)
    results = [c for c in comments if c["video_id"] == video_id]

    print("\n--- Комментарии ---")
    if not results:
        print("Комментариев пока нет.")
        return

    for comment in results:
        print(f"{comment['author']}: {comment['text']}")
