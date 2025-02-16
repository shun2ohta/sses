## GitHub Desktop を使って履歴管理を行う［基本編］

公開: 2025-02-16 17:05:10


GitHub Desktop というアプリケーションがあり、これでもリポジトリの履歴を管理することができます。具体的には、「History」タブを見ると、どんな変更をしたのかふりかえることが可能で、メニューから選んだり、右クリック（ダブルタップ）して、やりたいことを選ぶだけです。このドキュメントは、<ins>リポジトリを作成し、main に Commit、Push するまで</ins>を扱うためにあります。


### 0. 事前に行うこと
-   GitHub の [アカウントを作成](https://docs.github.com/ja/get-started/start-your-journey/creating-an-account-on-github) します
-	GitHub Desktop を [公式サイト](https://docs.github.com/ja/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop) の指示にしたがい、ダウンロード、インストールします
-	GitHub Desktop にログイン（GitHub Desktop → Settings → Account からログイン）します

### 1. GitHub Desktop でリポジトリのクローンをつくる
-	GitHub Desktop を開きます
-	[File] → [Clone repository] を選択します
-	[GitHub.com] タブを選択します
-	自分で作成したり、招待を受けたりしたリポジトリがリストに表示されているので、クローンを作成したいリポジトリを選択します
-	クローン先のディレクトリを指定します（`~/Documents/GitHub/` の下に作成することが多いです＝デフォルトのままで問題ありません）
-	[Clone] をクリックします
-	クローンが完了すると、ローカルにリポジトリのコピーが作成されます

✔ ポイント
-	クローンとは GitHub 上のリポジトリ（リモートリポジトリと呼びます）を 自分のマシン（ローカル）にコピーすること
-	ローカルで作業した内容は、リモートリポジトリ に反映できるようになる


### 2. クローンしたローカルディレクトリに変更を加える
-   何かファイルをクローンしたローカルディレクトリに置いてみます
-	適当なファイルを編集してみます

✔ ポイント
-	編集作業そのものを必ずローカルディレクトリのなかで行う
-	4番以降を実行するまでは変更履歴を他の誰もみることはできない


### 3. Commit する
-	GitHub Desktop を開きます → 変更が検出されています
-	Summary 欄に変更内容を説明するメッセージを入力（例: 東京の気候値を追加）します
-	[Commit to main] をクリックします

✔ ポイント
-	Commit は変更をローカルに保存すること
-	Commit してもまだ GitHub にはアップロードされていない


### 4. Push して GitHub に反映
-	右上の [Push origin] をクリックします
-	"Push completed successfully" と表示されます（Pushできました！）
-	GitHub の Web ページでリポジトリを開き、変更が反映されたことを確認します

✔ ポイント
-	Push はローカルの変更を GitHub にアップロードすること
-	他のメンバーもこの変更をみることができるので、以降共同での作業が可能となる