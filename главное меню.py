from auth import register, login
from videos import list_videos, add_video, delete_video, like_video, search_videos
from comments import add_comment, show_comments
from users import show_profile

def pause():
    input("\nНажмите Enter, чтобы продолжить...")

def guest_menu():
    while True:
        print("\n" + "=" * 40)
        print("             CLIPZONE")
        print("      Платформа коротких видео")
        print("=" * 40)
        print("1. Регистрация")
        print("2. Войти")
        print("3. Смотреть ленту")
        print("4. Найти видео")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                user_menu(username)
        elif choice == "3":
            list_videos()
            pause()
        elif choice == "4":
            search_videos()
            pause()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")

def user_menu(username):
    while True:
        print("\n" + "=" * 40)
        print(f"        ПОЛЬЗОВАТЕЛЬ: {username}")
        print("=" * 40)
        print("1. Смотреть ленту")
        print("2. Добавить видео")
        print("3. Мои видео")
        print("4. Поставить/убрать лайк")
        print("5. Добавить комментарий")
        print("6. Посмотреть комментарии")
        print("7. Мой профиль")
        print("8. Найти видео")
        print("9. Удалить моё видео")
        print("0. Выйти из аккаунта")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            list_videos()
            pause()
        elif choice == "2":
            add_video(username)
        elif choice == "3":
            list_videos(author=username)
            pause()
        elif choice == "4":
            list_videos()
            video_id = input("Введите ID видео: ").strip()
            like_video(video_id, username)
            pause()
        elif choice == "5":
            list_videos()
            video_id = input("Введите ID видео: ").strip()
            add_comment(video_id, username)
        elif choice == "6":
            video_id = input("Введите ID видео: ").strip()
            show_comments(video_id)
            pause()
        elif choice == "7":
            show_profile(username)
            pause()
        elif choice == "8":
            search_videos()
            pause()
        elif choice == "9":
            list_videos(author=username)
            video_id = input("Введите ID видео: ").strip()
            delete_video(video_id, username)
            pause()
        elif choice == "0":
            print("Вы вышли из аккаунта.")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    guest_menu()