# Made by svenskithesource#2815

import requests, time, random, string, os


def find():
    with open("streamable_failed.txt", "r") as f:
        lines = [line.rstrip() for line in f.readlines() if line != "\n"]
    random_code = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    url = "https://streamable.com/" + random_code
    if url not in lines:
        req = requests.get(url)
        return {"url": url, "status_code": req.status_code}
    else:
        return {"url": url, "status_code": 400}


def main():
    if not os.path.exists("./streamable.txt"):
        open("streamable.txt", "w").close()

    if not os.path.exists("./streamable_failed.txt"):
        open("streamable_failed.txt", "w").close()

    while True:
        find_streamable = find()
        if find_streamable["status_code"] == 200:
            with open("streamable.txt", "a") as f:
                f.write(find_streamable["url"] + "\n")
            print(find_streamable["url"])
        elif find_streamable["status_code"] == 429:
            print("Getting rate limited! Waiting 1 min.")
            time.sleep(60)
            print("Starting again!")
        elif find_streamable["status_code"] == 404:
            with open("streamable_failed.txt", "a") as f:
                f.write(find_streamable["url"] + "\n")
        else:
            print("Failed", find_streamable["url"])


if __name__ == '__main__':
    main()
