#!/usr/bin/python3

import os
from datetime import datetime
import re

readme_path = "README.md"
memo_dir = "memo"
base_url = "https://www.gesw.org/memo/"

def format_datetime(dt_str):
    try:
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%Y年%m月%d日%H時")
    except ValueError:
        return dt_str

def extract_metadata(filepath):
    """Markdownからタイトル, 公開(ISO), 更新(ISO)を返す"""
    title = None
    published_iso = None
    updated_iso = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if re.match(r"^#{1,2} ", line):
                title = re.sub(r"^#{1,2} ", "", line).strip()
            elif line.startswith("公開:"):
                m = re.match(
                    r"公開: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})(（更新: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})）)?",
                    line
                )
                if m:
                    published_iso = m.group(1)
                    updated_iso = m.group(3) if m.group(3) else None
            if title and published_iso:
                break

    return title, published_iso, updated_iso

def update_readme_with_links():
    md_files = [f for f in os.listdir(memo_dir) if f.endswith(".md")]

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.readlines()
    else:
        readme_content = []

    # 各エントリは (published_iso_datetime, link_str) にする
    entries = []

    for md_file in md_files:
        file_path = os.path.join(memo_dir, md_file)
        title, pub_iso, upd_iso = extract_metadata(file_path)

        if not pub_iso:
            print(f"警告: {md_file} に公開日時がありません。スキップします。")
            continue

        # 文字列→datetime（ソート用）
        try:
            pub_dt = datetime.strptime(pub_iso, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print(f"警告: {md_file} の公開日時の形式が不正です。スキップします。")
            continue

        # 表示用に整形
        pub_disp = format_datetime(pub_iso)
        upd_disp = format_datetime(upd_iso) if upd_iso else None
        if not upd_disp:
            upd_disp = pub_disp

        if not title:
            title = md_file.replace(".md", "")

        html_file = md_file.replace(".md", ".html")
        link_url = f"{base_url}{html_file}"

        if upd_disp == pub_disp:
            link_str = f"- [{title}]({link_url})（{pub_disp}公開）\n"
        else:
            link_str = f"- [{title}]({link_url})（{pub_disp}公開、{upd_disp}更新）\n"

        entries.append((pub_dt, link_str))

    # 公開日時（datetime）で降順にソート
    entries.sort(key=lambda x: x[0], reverse=True)

    # README.md を再構築
    non_link_content = [line for line in readme_content if not line.startswith("- [")]
    updated_links = [link for _, link in entries]
    final_content = non_link_content + updated_links

    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(final_content)

    print(f"README.md updated with {len(updated_links)} links, sorted by publication date.")

if __name__ == "__main__":
    update_readme_with_links()