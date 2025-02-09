## Visual Studio Code + Anaconda 環境の構築

公開: 2025-02-09 11:57:42


Visual Studio Code（VSCode）ベースで簡易な開発環境をローカルにつくります。なるべく手数が少ないことが条件で、以降レヴェルに応じてカスタマイズをしやすい方法を選択します。

1. VSCode をインストールする

VSCodeを[サイトからダウンロード](https://azure.microsoft.com/ja-jp/products/visual-studio-code)します。Mac版Apple Siliconeのzipファイルを選ぶとよいでしょう。Application/ にインストールし、好みでDockに追加しておきます。なお、同時に Command line Tools もインストールしておきます。

2. VSCode をエディタとして使い、OS標準のpythonで使う

画面左側の拡張機能のロゴをクリックして「python」と検索します。Microsoft の python 関係のツールだけで構わないのでインストールします（8〜9個あります）。組み込み関数や標準ライブラリ（random, csv など）を使うだけの場合はこれで問題ありません。なお、OS標準でインストールされているpythonは、`/usr/bin/python3` です。

3. Anaconda 環境をインストールし、一般的なライブラリを活用する

matplotlib や NumPy, pandas などの外部ライブラリを個別にインストールしてももちろん問題はないですが、Anacondaで一括インストールするほうが楽で研究室内で環境を統一しやすいです。

[Anacondaのサイト](https://www.anaconda.com/download)から、Mac版64ビットApple Silicone用の`Anaconda3-*-MacOSX-arm64.pkg`をダウンロードしてインストールします。インストール後にAnacondaを開くとアップデートするかどうか聞かれます。アップデートしてもいいですが、Navigatorを利用する予定はないので、どちらでも構いません。また、その後「sign in」画面が出てきますが、何もしないで Navigator 自体も終了してください。

VSCodeを再度立ち上げる（Anacondaをインストールしてから再度立ち上げ直してください）と、PATHが通っているので、インストール済みの外部ライブラリはすでに利用できる状態になっています。まずはカーネルで `Base (Python 3.*)` を選択する必要があります。