import requests
import re
import json
import csv

session = requests.Session()

url = "https://fund.eastmoney.com/js/fundcode_search.js"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

resp = session.get(url, headers=headers, timeout=15)

print("URL:", resp.url)
print("STATUS:", resp.status_code)
print("PREVIEW:", resp.text[:200])

# 1. 去掉 var r =
json_text = re.sub(r'^var\s+r\s*=\s*', '', resp.text).strip()

# 2. 去掉末尾分号（如果有）
if json_text.endswith(';'):
    json_text = json_text[:-1]

# 3. 转 JSON
data = json.loads(json_text)

data_list = []

for item in data:
    data_list.append((item[0], item[2]))

with open("east_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["基金代码", "基金名称"])
    writer.writerows(data_list)

print("基金数量:", len(data))
print("前5条:", data[:5])
