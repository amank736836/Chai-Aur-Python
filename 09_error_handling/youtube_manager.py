import json


def load_data():
    try:
        with open("youtube_data.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("youtube_data.txt", "w") as file:
            json.dump([], file)
        return []


def save_data_helper(videos):
    with open("youtube_data.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(
            f"{index}. {video['title']} - {video['views']} views - {video['time']} minutes"
        )


def add_video(videos):
    print("-" * 25)

    title = input("Enter the title of the video: ")

    if not title:
        print("Title should not be empty")
        return
    elif any(video["title"] == title for video in videos):
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

    video = {"title": title, "views": views, "time": time}
    videos.append(video)
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
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
        elif any(video["title"] == title for video in videos):
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

        video = {"title": title, "views": views, "time": time}
        videos[index - 1] = video
        save_data_helper(videos)
    else:
        print("Invalid index")


def delete_video(videos):
    list_all_videos(videos)
    print("-" * 25)
    index = input("Enter the index of the video to delete: ")

    if not index.isdigit():
        print("Index should be a number")
        return
    else:
        index = int(index)

    if 1 <= index <= len(videos):
        # videos.pop(index - 1)
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index")


def main():
    videos = load_data()
    while True:
        print("-" * 25)
        print("\n Youtube Manager")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video Details")
        print("4. Delete a Youtube video")
        print("5. Exit the application")
        print("-" * 25)
        choice = input("Enter your choice: ")
        print("-" * 25)

        match choice:
            case "1":
                print("\nListing all Youtube videos")
                list_all_videos(videos)
            case "2":
                print("Adding a Youtube video")
                add_video(videos)
            case "3":
                print("Updating a Youtube video")
                update_video(videos)
            case "4":
                print("Deleting a Youtube video")
                delete_video(videos)
            case "5":
                print("Exiting the application")
                print("-" * 25)
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
