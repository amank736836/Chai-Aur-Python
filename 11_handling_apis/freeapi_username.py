import requests


def fetch_random_user_freeapi():
    try:
        url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
        response = requests.get(url)
        data = response.json()

        if data["success"] and "data" in data:
            user_data = data["data"]
            username = user_data["login"]["username"]
            country = user_data["location"]["country"]
            return username, country
        else:
            raise Exception("Failed to fetch user data from API")
    except Exception as e:
        print(f"Error: {e}")


def main():
    username, country = fetch_random_user_freeapi()
    print(f"Username: {username}")
    print(f"Country: {country}")


if __name__ == "__main__":
    main()
