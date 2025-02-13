#!/usr/bin/python3

import sys
import re
from datetime import datetime

def update_timestamp(file_path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # ファイルを読み込む
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()

        # タイトル行を探す（最初の `#` で始まる行）
        title_index = next((i for i, line in enumerate(content) if line.lstrip().startswith("#")), None)

        if title_index is None:
            print("Error: No title (#) found in the file.")
            sys.exit(1)

        # 公開日時の行を探す
        publish_index = next((i for i, line in enumerate(content) if line.startswith("公開:")), None)

        if publish_index is None:
            # 初回: 公開日時をタイトル直下に挿入
            content.insert(title_index + 1, f"\n公開: {now}\n\n")
        else:
            # 既存の公開日時の行を取得
            existing_publish_line = content[publish_index].strip()

            # 既存の公開日時の取得（更新部分を除去）
            existing_publish_time = re.sub(r"（更新: .*?）", "", existing_publish_line).replace("公開:", "").strip()

            # 公開日時 + 最新の更新日時のみを保持
            updated_line = f"公開: {existing_publish_time}（更新: {now}）\n"
            content[publish_index] = updated_line  # 公開日時の行を更新

        # 修正した内容をファイルに書き戻す
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(content)

        print(f"Timestamp updated successfully in {file_path}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# VSCodeのターミナルからファイルパスを取得
if len(sys.argv) < 2:
    print("Usage: python update_timestamp.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
update_timestamp(file_path)