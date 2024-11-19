import os
import re
from datetime import datetime

# README.md のパス
readme_path = "README.md"
# メモディレクトリのパス
memo_dir = "memo"
# 公開リンクのベースURL
base_url = "https://www.gesw.org/memo/"

def extract_timestamps(filepath):
    """Markdownファイルから公開日時と更新日時を抽出"""
    published = None
    updated = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("公開:"):
                published = line.replace("公開:", "").strip()
            elif line.startswith("更新:"):
                updated = line.replace("更新:", "").strip()
            # 公開と更新が見つかれば解析を終了
            if published and updated:
                break

    return published, updated

def update_readme_with_links():
    # memo/ 以下の .md ファイルを取得
    md_files = [f for f in os.listdir(memo_dir) if f.endswith(".md")]

    # README.md の既存内容を読み込む
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.readlines()
    else:
        readme_content = []

    # README.md に記載するリンクを構築
    updated_links = []
    for md_file in md_files:
        file_path = os.path.join(memo_dir, md_file)

        # 公開日時と更新日時を抽出
        published_time, updated_time = extract_timestamps(file_path)
        if not published_time:
            print(f"警告: {md_file} に公開日時がありません。スキップします。")
            continue

        # 更新日時がない場合は公開日時を使用
        if not updated_time:
            updated_time = published_time

        # HTMLリンク形式を生成
        html_file = md_file.replace(".md", ".html")
        link_url = f"{base_url}{html_file}"

        # 公開日時と更新日時のフォーマットによるリンク生成
        if published_time == updated_time:
            updated_links.append(
                f"- [{md_file.replace('.md', '')}]({link_url})（{published_time}公開）\n"
            )
        else:
            updated_links.append(
                f"- [{md_file.replace('.md', '')}]({link_url})（{published_time}公開、{updated_time}更新）\n"
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