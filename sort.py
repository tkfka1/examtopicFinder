import json


# JSON 파일 열기
with open('on.json', 'r') as f:
    data = json.load(f)

with open('output.txt', 'w') as f:
    for key in data:
        for url in data[key]:
            print(f"{key}. {url}")
            f.write(f"{key}. {url}\n")