import requests


class ReqMaker:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/youtube/v3/search"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def list_videos(
        self,
        key,
        q="Pizza",
        max_results=25,
        part="snippet",
        order="date",
        qtype="video",
        published_after="2019-01-01T00:00:00Z",
    ):

        params = {
            "q": q,
            "key": key,
            "type": qtype,
            "part": part,
            "order": order,
            "maxResults": max_results,
            "publishedAfter": published_after,
        }

        res = requests.get(self.base_url, headers=self.headers, params=params)

        return res.json()
