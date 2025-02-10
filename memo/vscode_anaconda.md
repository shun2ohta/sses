## Visual Studio Code + Anaconda で開発環境を構築する

公開: 2025-02-09 11:57:42


Visual Studio Code（VSCode）ベースで簡易な開発環境をローカルにつくります。なるべく手数が少ないことが条件で、以降レヴェルに応じてカスタマイズをしやすい方法を選択します。以下の最低限のインストールと好みの調整にかかる時間は20〜30分程度です。

### 1. VSCode をインストールする

VSCodeを[サイトからダウンロード](https://code.visualstudio.com/Download#)します。Mac版Apple Siliconeのzipファイルを選ぶとよいでしょう。解凍後、Application/ にインストールし（＝移動させ）、好みでDockに追加しておきます。なお、Pythonの機能拡張をインストールすると自動的に Xcode の Command line developer tools のインストールを促してくるので、指示にしたがってインストールしておきます（Appleによる機能です）。
![Command Line Developer Tools](https://www.gesw.org/img/memo/InstallCommandLineTools.png)

### 2. VSCode をエディタとして使い、OS標準の Python を使う

画面左側の拡張機能のロゴをクリックして「python」と検索します。Microsoft の Python 関係のツールだけで構わないのでインストールします（4〜5個ありますが、本体のpythonをインストールすると自動で関連する拡張機能もインストールされます）。組み込み関数や標準ライブラリ（random, csv など）を使うだけの場合はこれで問題ありません。なお、macOS標準でインストールされているpythonは、`/usr/bin/python3` です。Version 2 までの `/usr/bin/python` ではないので、注意が必要です。
    
実習用の環境は Google Colab であるので、Jupyter Notebook の機能拡張（4個; 「Jupyter」で検索し、まずはMicrosoftの標準のものをインストールするだけで構いません）もインストールします。これだけで、Jupyter Notebook のファイル（ipynb）を扱うことができます。最初に実行すると、ipy kernel をインストールするように促されますので、指示にしたがいます。
    
蛇足ですが、無料で Copilot も使えるので、おすすめにしたがって機能拡張をインストールしておくとよいでしょう（2025年1月現在で、デフォルトが ChatGPT 4oです）。もちろん必須ではないです。

### 3. Anaconda 環境をインストールし、一般的なライブラリを VSCode 経由で活用する

matplotlib や NumPy、pandas などの外部ライブラリを個別にインストールしてももちろん問題はないですが、Anacondaで一括インストールするほうが依存関係やヴァージョン違いが少なく、研究室内で環境を統一しやすいです。

[Anacondaのサイト](https://www.anaconda.com/download)から、Mac版64ビットApple Silicone用の`Anaconda3-*-MacOSX-arm64.pkg`をダウンロードしてインストールします。登録画面から電子メイルアドレスを入力すると、ダウンロードサイトが書かれたメイルが送られてきます。インストール後にAnacondaを開くとアップデートするかどうか聞かれます。アップデートしてもいいですが、Navigatorを利用する予定はないので、どちらでも構いません。また、その後「Sign in」画面が出てきますが、何もしないで Navigator 自体も終了してください。

VSCodeを再度立ち上げる（Anacondaをインストールしてから再度立ち上げ直してください）と、PATHが通っているので、インストール済みの外部ライブラリはすでに利用できる状態になっています。まずはカーネルで `Base (Python 3.*)` を選択する必要があります。
    
### 4. VSCode を使って開発を行う

コードを書いたり、実行したりする際に、Anacondaを意識する必要は特段ありません。