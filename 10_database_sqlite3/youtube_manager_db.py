import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        views INTEGER NOT NULL,
        time INTEGER NOT NULL
    )
    """)


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    for video in videos:
        print(f"{video[0]}. {video[1]} - {video[2]} views - {video[3]} minutes")

    return videos


def add_video():
    print("-" * 25)

    title = input("Enter the title of the video: ")

    if not title:
        print("Title should not be empty")
        return

    views = input("Enter the number of views: ")

    if not views:
        print("Views should not be empty")
        return
    elif views.isdigit() is False:
        print("Views should be a number")
        return
    elif int(views) < 0:
        print("Views should be a positive number")
        return

    time = input("Enter the time of the video: ")

    if not time:
        print("Time should not be empty")
        return
    elif time.isdigit() is False:
        print("Time should be a number")
        return
    elif int(time) < 0:
        print("Time should be a positive number")
        return

    videos = cursor.fetchall()
    if any(video["title"] == title for video in videos):
        print("Title already exists")
        return

    cursor.execute(
        "INSERT INTO videos (title, views, time) VALUES (?, ?, ?)", (title, views, time)
    )
    conn.commit()


def update_video():
    videos = list_all_videos()
    print("-" * 25)
    index = input("Enter the index of the video to update: ")

    if not index.isdigit():
        print("Index should be a number")
        return
    else:
        index = int(index)

    if 1 <= index <= len(videos):
        title = input("Enter the title of the video: ")

        if not title:
            print("Title should not be empty")
            return
        elif any(video[0] == title for video in videos):
            print("Title already exists")
            return

        views = input("Enter the number of views: ")

        if not views:
            print("Views should not be empty")
            return
        elif views.isdigit() is False:
            print("Views should be a number")
            return
        elif int(views) < 0:
            print("Views should be a positive number")
            return

        time = input("Enter the time of the video: ")

        if not time:
            print("Time should not be empty")
            return
        elif time.isdigit() is False:
            print("Time should be a number")
            return
        elif int(time) < 0:
            print("Time should be a positive number")
            return

        cursor.execute(
            "UPDATE videos SET title = ?, views = ?, time = ? WHERE id = ?",
            (title, views, time, index),
        )
        conn.commit()

    else:
        print("Invalid index")


def delete_video():
    videos = list_all_videos()
    print("-" * 25)
    index = input("Enter the index of the video to delete: ")

    if not index.isdigit():
        print("Index should be a number")
        return
    else:
        index = int(index)

    if 1 <= index <= len(videos):
        cursor.execute("DELETE FROM videos WHERE id = ?", (index,))
        conn.commit()
    else:
        print("Invalid index")


def main():
    while True:
        print("-" * 25)
        print("\n Youtube Manager - SQLite3")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video Details")
        print("4. Delete a Youtube video")
        print("5. Exit the application")
        print("-" * 25)
        choice = input("Enter your choice: ")
        print("-" * 25)

        if choice == "1":
            print("\nListing all Youtube videos")
            list_all_videos()
        elif choice == "2":
            print("Adding a Youtube video")
            add_video()
        elif choice == "3":
            print("Updating a Youtube video")
            update_video()
        elif choice == "4":
            print("Deleting a Youtube video")
            delete_video()
        elif choice == "5":
            print("Exiting the application")
            print("-" * 25)
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
