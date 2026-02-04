import re
import time

import pandas as pd
from DrissionPage import ChromiumPage

pattern = r'(\d+)\t(\d+)\t(.*?)\t.*?\t.*?\n'


def get_code_name(text):
    match = re.search(pattern, text)
    if match:
        fund_code = match.group(2)
        fund_name = match.group(3)
        return fund_code, fund_name
    else:
        return None, None


def fetch_funds():
    # 1. 启动并打开网页
    page = ChromiumPage()
    print("正在访问页面...")
    page.get('https://www.fund123.cn/fund')

    all_data = []
    page_num = 1

    try:
        while page_num <= 962:
            print(f"正在抓取第 {page_num} 页...")
            # 等待表格加载
            page.wait.ele_displayed('tag:table')

            current_data = []

            # 获取所有行
            rows = page.eles('tag:tr')[1:]  # 跳过表头
            for row in rows:
                text = row.raw_text
                code_name = get_code_name(text)
                current_data.append(code_name)
                all_data.append(code_name)

            if len(current_data) != 20:
                print(page_num, current_data)

            # 4. 寻找“下一页”按钮 (符号为 >)
            # 这里的定位逻辑：查找 class 包含 'next' 的元素，或者包含 '>' 字符的按钮
            # 或者是特定的分页图标类名
            next_btn = page.ele('. ant-pagination-next')
            # 5. 判断是否还能点击下一页
            # 如果按钮不存在，或者按钮带有 'disabled' 属性/类名，则停止
            print("点击下一页...")
            next_btn.click()
            page_num += 1
            time.sleep(0.2)  # 等待数据加载
    except Exception as e:
        print(f"运行出错: {e}")

    # 6. 保存数据
    if all_data:
        df = pd.DataFrame(all_data, columns=['基金代码', '基金名称'])
        # 去重处理
        df.drop_duplicates(inplace=True)
        df.to_csv("ant_data.csv", index=False, encoding="utf-8-sig")
        print(f"抓取结束！共获得 {len(df)} 条不重复数据，已保存至 ant_data.csv")
    else:
        print("未抓取到任何数据。")

    page.quit()


if __name__ == "__main__":
    fetch_funds()
