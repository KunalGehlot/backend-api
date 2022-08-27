import requests

BASE_URL = "https://www.googleapis.com/youtube/v3/search"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


async def list_videos(
    key,
    q="Pizza",
    order="date",
    qtype="video",
    max_results=25,
    part="snippet",
    published_after="2019-01-01T00:00:00Z",
) -> requests.Response:

    params = {
        "q": q,
        "key": key,
        "type": qtype,
        "part": part,
        "order": order,
        "maxResults": max_results,
        "publishedAfter": published_after,
    }

    res = await requests.get(BASE_URL, headers=HEADERS, params=params)

    return res
