import os

# README.md のパス
readme_path = "README.md"
# メモディレクトリのパス
memo_dir = "memo"
# 公開リンクのベースURL
base_url = "https://www.gesw.org/memo/"

def update_readme_with_links():
    # memo/ 以下の .md ファイルを取得
    md_files = [
        f for f in os.listdir(memo_dir)
        if f.endswith(".md")
    ]

    # ファイルが見つからなかった場合
    if not md_files:
        print("No .md files found in memo/ directory.")
        return

    # README.md の既存内容を読み込む
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.readlines()
    else:
        readme_content = []

    # README.md に追加するリンクのリストを作成
    new_links = []
    for md_file in md_files:
        file_path = os.path.join(memo_dir, md_file)
        
        # ファイルの1行目を取得
        with open(file_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
        
        # `#` を無視した内容を取得
        cleaned_line = first_line.lstrip("#").strip()
        
        # HTMLリンク形式を生成
        html_file = md_file.replace(".md", ".html")
        link = f"- [{cleaned_line}]({base_url}{html_file})\n"
        
        # 重複チェック
        if link not in readme_content:
            new_links.append(link)

    # 新しいリンクを README.md に追記
    if new_links:
        with open(readme_path, "a", encoding="utf-8") as f:
            f.writelines(new_links)
        print(f"Added {len(new_links)} new links to {readme_path}.")
    else:
        print("No new links to add.")

if __name__ == "__main__":
    update_readme_with_links()
