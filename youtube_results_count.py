import re
import requests

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ko-KR,ko;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"123.0.6312.106\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"123.0.6312.106\", \"Not:A-Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"123.0.6312.106\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "service-worker-navigation-preload": "true",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

cookies = {
    "GPS": "1",
    "YSC": "A5IaJeQujfs",
    "VISITOR_INFO1_LIVE": "5LdFUWHYcEM",
    "VISITOR_PRIVACY_METADATA": "CgJLUhIEGgAgYg==",
    "PREF": "tz=Asia.Seoul"
}

query = "굽네치킨"
response = requests.get(f"https://www.youtube.com/results?search_query={query}", headers=headers, cookies=cookies)
keyword = re.findall(r'"refinements":\s*(\[[^\]]*\])', response.text)
print(keyword)
matches = re.findall(r'"estimatedResults":"(\d+)"', response.text)

if matches:
    print("Estimated Results:", matches[0])  # 첫 번째 매칭 결과 출력
else:
    print("Estimated results not found in the HTML response.")