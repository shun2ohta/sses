#!/usr/bin/python3

import re
from datetime import datetime
import sys

def update_timestamp(file_path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    publish_line = f"公開: {now}\n"
    update_line = f"更新: {now}\n"

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
        publish_exists = any(line.startswith("公開:") for line in content)

        if not publish_exists:
            # 初回: 公開日時をタイトル直下に挿入
            content.insert(title_index + 1, f"\n{publish_line}\n")
        else:
            # 2回目以降: 公開日時は保持し、更新日時を管理
            content = [
                line for line in content if not line.startswith("更新:")
            ]  # 既存の更新日時を削除
            publish_index = next(
                i for i, line in enumerate(content) if line.startswith("公開:")
            )
            content.insert(publish_index + 1, f"{update_line}")

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