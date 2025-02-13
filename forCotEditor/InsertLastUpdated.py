#!/usr/bin/python3

import re
from datetime import datetime
import sys

def update_timestamp(file_path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # ファイルを読み込む
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()

        # タイトル行を探す（最初の `#` で始まる行）
        title_index = next((i for i, line in enumerate(content) if line.startswith("#")), None)

        if title_index is None:
            print("Error: No title (#) found in the file.")
            return

        # 公開日時が既に存在するか確認
        publish_index = next((i for i, line in enumerate(content) if line.startswith("公開:")), None)

        if publish_index is None:
            # 初回: 公開日時をタイトル直下に挿入
            publish_line = f"公開: {now}\n"
            content.insert(title_index + 1, f"\n{publish_line}\n")
        else:
            # 既存の公開日時を取得し、更新日時を管理
            existing_publish_line = content[publish_index].strip()

            # 既存の「（更新: YYYY-MM-DD HH:MM:SS）」を削除し、公開日時のみ取得
            publish_match = re.match(r"公開: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", existing_publish_line)
            if publish_match:
                formatted_publish_time = publish_match.group(1)  # 既存の公開日時を維持
                updated_line = f"公開: {formatted_publish_time}（更新: {now}）\n"
                content[publish_index] = updated_line  # 公開日時の行を更新
            else:
                # 既存の公開日時のフォーマットが不明な場合、新しく追加
                updated_line = f"公開: {now}\n"
                content[publish_index] = updated_line

        # 修正した内容をファイルに書き戻す
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(content)

        print("Timestamp updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

# CotEditorから渡された引数でファイルパスを取得
if len(sys.argv) < 2:
    print("Error: No file path provided. Run this script from CotEditor.")
else:
    file_path = sys.argv[1]
    update_timestamp(file_path)