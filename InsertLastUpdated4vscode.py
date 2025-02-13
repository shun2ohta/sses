#!/usr/bin/python3

import re
import sys
from datetime import datetime

def format_datetime(dt_str):
    """日時を 'YYYY年MM月DD日HH時MM分SS秒' に整形"""
    try:
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%Y年%m月%d日 %H:%M:%S")
    except ValueError:
        return dt_str  # フォーマットエラー時はそのまま返す

def update_timestamp(file_path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_now = format_datetime(now)

    try:
        # ファイルを読み込む
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()

        # タイトル行を探す（最初の `#` で始まる行）
        title_index = next((i for i, line in enumerate(content) if line.lstrip().startswith("#")), None)

        if title_index is None:
            print("Error: No title (#) found in the file.")
            sys.exit(1)

        # 公開日時が既に存在するか確認
        publish_index = next((i for i, line in enumerate(content) if line.startswith("公開:")), None)

        if publish_index is None:
            # 初回: 公開日時をタイトル直下に挿入
            content.insert(title_index + 1, f"\n公開: {formatted_now}\n\n")
        else:
            # 既存の公開日時を取得
            existing_publish_line = content[publish_index].strip()

            # 「公開: YYYY年MM月DD日HH時MM分SS秒」のフォーマットから日付部分を抽出
            publish_match = re.match(r"公開: (\d{4}年\d{2}月\d{2}日 \d{2}:\d{2}:\d{2})", existing_publish_line)
            if publish_match:
                formatted_publish_time = publish_match.group(1)  # 既存の公開日時を維持
                updated_line = f"公開: {formatted_publish_time}（更新: {formatted_now}）\n"
            else:
                # フォーマットが不明な場合、現在の時刻を公開日時とする
                updated_line = f"公開: {formatted_now}\n"

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