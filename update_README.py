import os
from datetime import datetime

# README.md のパス
readme_path = "README.md"
# メモディレクトリのパス
memo_dir = "memo"
# 公開リンクのベースURL
base_url = "https://www.gesw.org/memo/"

def extract_existing_links(content):
    """既存リンクから公開日時・更新日時情報を抽出"""
    links = []
    for i, line in enumerate(content):
        if line.startswith("- ["):
            # 公開日時と更新日時を抽出
            try:
                name_part, date_part = line.split("（")
                title = name_part.split("]")[0][3:]
                url = name_part.split("(")[1].split(")")[0]
                dates = date_part.strip("）\n").split("、")
                published = dates[0].replace("公開", "").strip()
                updated = dates[1].replace("更新", "").strip() if len(dates) > 1 else published
                links.append({
                    "title": title,
                    "url": url,
                    "published": published,
                    "updated": updated,
                    "line_index": i,
                    "line": line
                })
            except Exception:
                continue
    return links

def update_readme_with_links():
    # memo/ 以下の .md ファイルを取得し更新日時を確認
    md_files = [
        (f, os.path.getmtime(os.path.join(memo_dir, f)))
        for f in os.listdir(memo_dir)
        if f.endswith(".md")
    ]

    # 更新日時でソート（新しい順）
    sorted_files = sorted(md_files, key=lambda x: x[1], reverse=True)

    # README.md の既存内容を読み込む
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.readlines()
    else:
        readme_content = []

    existing_links = extract_existing_links(readme_content)
    updated_links = []

    for md_file, mtime in sorted_files:
        file_path = os.path.join(memo_dir, md_file)
        
        # ファイルの1行目を取得
        with open(file_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()

        # `#` を無視した内容を取得
        cleaned_line = first_line.lstrip("#").strip()

        # HTMLリンク形式を生成
        html_file = md_file.replace(".md", ".html")
        link_url = f"{base_url}{html_file}"

        # 更新日時を整形（YYYY年MM月DD日HH時）
        updated_time = datetime.fromtimestamp(mtime).strftime("%Y年%m月%d日%H時")

        # 既存リンクを探して公開日時を保持
        existing_link = next((link for link in existing_links if link["url"] == link_url), None)
        if existing_link:
            published_time = existing_link["published"]
            if published_time == updated_time:
                # 公開日時と更新日時が同じ場合
                updated_links.append(
                    f"- [{cleaned_line}]({link_url})（{published_time}公開）\n"
                )
            else:
                # 公開日時と更新日時が異なる場合
                updated_links.append(
                    f"- [{cleaned_line}]({link_url})（{published_time}公開、{updated_time}更新）\n"
                )
        else:
            # 新規リンクの場合、現在の更新日時を公開日時として追加
            updated_links.append(
                f"- [{cleaned_line}]({link_url})（{updated_time}公開）\n"
            )

    # 公開日時順（新しい順）で並び替え
    updated_links = sorted(updated_links, key=lambda x: x.split("（")[1].split("公開")[0].strip(), reverse=True)

    # README.md を再構築
    non_link_content = [line for line in readme_content if not line.startswith("- [")]
    final_content = non_link_content + updated_links

    # README.md を上書き
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(final_content)

    print(f"README.md updated with {len(updated_links)} links, sorted by publication date.")

if __name__ == "__main__":
    update_readme_with_links()
