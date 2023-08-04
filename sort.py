import json

# JSON 파일 열기
with open('on.json', 'r') as f:
    data = json.load(f)

print(data)


def txt50(t):
    with open(f"output{t}.txt", 'w') as f:
        a = t
        for key in range(t,t+50,1):
            if key == len(data):
                break
            for url in data[str(key)]:
                print(f"{key}. {url}")
                f.write(f"{key}. {url}\n")
            
            if key == t == 0:
                print(f"end {key}")

count = 0
for i in data:
    for ii in i:
        count += 1
print(count)


for i in range(0,len(data),50):
    if i == 0:
        i = 1
    print(i)
    txt50(i)

# with open('output.txt', 'w') as f:
#     for key in data:
#         for url in data[key]:
#             print(f"{key}. {url}")
#             f.write(f"{key}. {url}\n")