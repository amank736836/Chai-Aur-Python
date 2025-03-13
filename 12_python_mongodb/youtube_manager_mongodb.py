# import pymongo
from pymongo import MongoClient
from bson import ObjectId

# Not a good idea to hardcode the password in the code
# Instead, use environment variables to store the password

try:
    client = MongoClient(
        "mongodb+srv://<username>:<password>@learning.iewcule.mongodb.net/"
    )
    print("-" * 25)
    print("Connected to MongoDB")
except Exception as e:
    print("Error connecting to MongoDB")
    print(e)


yt_manager_db = client["yt_manager"]
video_collection = yt_manager_db["videos"]


def list_all_videos():
    videos = video_collection.find()
    for video in videos:
        print(
            f"{video['_id']} - {video['title']} - {video['views']} views - {video['time']} minutes"
        )
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

    videos = video_collection.find()
    if any(video["title"] == title for video in videos):
        print("Title already exists")
        return

    video_collection.insert_one({"title": title, "views": views, "time": time})


def update_video():
    videos = list_all_videos()
    print("-" * 25)
    id = input("Enter the id of the video to update: ")

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

    response = video_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"title": title, "views": views, "time": time}},
    )

    if response.modified_count == 0:
        print("Invalid id")
        return
    else:
        print("Video updated successfully")


def delete_video():
    videos = list_all_videos()
    print("-" * 25)
    id = input("Enter the id of the video to delete: ")

    response = video_collection.delete_one({"_id": ObjectId(id)})

    if response.deleted_count == 0:
        print("Invalid id")
        return
    else:
        print("Video deleted successfully")


def main():
    while True:
        print("-" * 25)
        print("Youtube Manager - MongoDB")
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

    client.close()


if __name__ == "__main__":
    main()
