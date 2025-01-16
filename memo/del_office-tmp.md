## WordやExcel, PwoerPointの一時ファイルを追跡しないようにする

公開: 2025-01-17 00:36:28


卒論など、フォーマットが決められたものではWordなどのアプリケーションを使わざるを得ないです。不可視の一時ファイルがファイルを開いて入り限りは残っているので、gitの追跡対象となります。これを除外するようにしたいです。

---------
# OS-generated files
.DS_Store

# Word temporary
~$*.doc*

# Word Auto Backup File
Backup of *.doc*

# Excel temporary
~$*.xls*

# Excel Backup File
*.xlk

# PowerPoint temporary
~$*.ppt*