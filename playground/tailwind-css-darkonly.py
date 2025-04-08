from bs4 import BeautifulSoup
import re

# カテゴリごとに判定できるようプレフィックスリスト
CATEGORIES = ['text-', 'bg-', 'border-', 'fill-', 'stroke-', 'outline-']

def get_category(cls):
    for prefix in CATEGORIES:
        if cls.startswith(prefix):
            return prefix
    return None

def replace_dark_classes(html):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all(class_=True):
        class_list = tag.get("class")
        if not class_list:
            continue

        dark_map = {}
        normal_map = {}

        # 分類：通常クラス / dark:クラス をカテゴリ単位で分ける
        for cls in class_list:
            if cls.startswith("dark:"):
                dark_cls = cls[5:]
                cat = get_category(dark_cls)
                if cat:
                    dark_map[cat] = dark_cls
            else:
                cat = get_category(cls)
                if cat:
                    normal_map.setdefault(cat, []).append(cls)
                else:
                    normal_map.setdefault("other", []).append(cls)

        # dark: のカテゴリに該当する通常クラスは除外（上書き対象）
        final_classes = normal_map.get("other", [])  # "その他" は常に保持

        for cat, classes in normal_map.items():
            if cat == "other":
                continue
            if cat in dark_map:
                continue  # dark: があるカテゴリは通常版除外
            final_classes.extend(classes)

        # 最後に dark: のクラスを通常クラスとして追加
        final_classes.extend(dark_map.values())

        tag['class'] = final_classes

    return str(soup)

# --- 使用例 ---

with open(input("Input HTML:"), "r", encoding="utf-8") as f:
    html = f.read()

modified_html = replace_dark_classes(html)

with open(input("Ouput HTML:"), "w", encoding="utf-8") as f:
    f.write(modified_html)
