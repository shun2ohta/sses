## GitHub Desktop を使って履歴管理を行う［基本編］

公開: 2025-02-16 17:05:10


GitHub Desktop というアプリケーションがあり、これでもリポジトリの履歴を管理することができます。具体的には、「History」タブを見ると、どんな変更をしたのかふりかえることが可能で、メニューから選んだり、右クリック（ダブルタップ）して、やりたいことを選ぶだけです。このドキュメントは、<ins>リポジトリを作成し、main に Commit、Push、Pull をして最新状態に保つまで</ins>を扱うためにあります。

なお、GitHub Desktop というときには、アプリケーションのことを指し、単に GitHub というときには、Web 版の リモートの GitHub 本体のことを指します。


### 0. 事前に行うこと
-   GitHub の [アカウントを作成](https://docs.github.com/ja/get-started/start-your-journey/creating-an-account-on-github) します
-	GitHub Desktop を [公式サイト](https://docs.github.com/ja/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop) の指示にしたがい、ダウンロード、インストールします
-	GitHub Desktop にログイン（[GitHub Desktop → Settings → Account からログイン](https://docs.github.com/ja/desktop/installing-and-authenticating-to-github-desktop/authenticating-to-github-in-github-desktop)）します

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
-	ローカルで作業した内容がリモートリポジトリに反映されるようになる

<div style="text-align: center;">
<img src="https://www.gesw.org/img/memo/Clone_a_Repository.png" alt="Clone_a_Repository" width="50%">
</div>

**図1. リポジトリのクローンをつくる**　自分で作成したリポジトリや招待されたリポジトリのみクローンをつくることができます。

### 2. クローンしたローカルディレクトリに変更を加える
-   何かファイルをクローンしたローカルディレクトリに置いてみます
-	適当なファイルを　CotEditor や VSCode などで編集してみます（他のアプリケーションを使うときと同様に、適宜保存してください）

✔ ポイント
-	編集作業そのものを必ずローカルディレクトリのなかで行う
-	4番以降を実行するまでは変更過程を他の誰もみることはできないので安心してよい

<div style="text-align: center;">
<img src="https://www.gesw.org/img/memo/Finder_OpenFile.png" alt="Finder_OpenFile" width="50%">
</div>

**図2. ローカルディレクトリでで編集作業を行う**　Finderでファイルを新たに置いたり（この例では、svgファイル）、編集したりすることができます。README.md を開くと次の図3のようになります。

<div style="text-align: center;">
<img src="https://www.gesw.org/img/memo/EditingFile.png" alt="EditingFile" width="50%">
</div>

**図3. VSCodeのエディタで編集作業を行う**　エディタは好みのものでよく、これに限りません。この例では、README.md に1行追記しています。


### 3. Commit する
-	GitHub Desktop を開きます → 変更が検出されています
-	Summary 欄に変更内容を説明するメッセージを入力（例: 東京の気候値を追加）します
-	[Commit to main] をクリックします

✔ ポイント
-	Commit は変更内容をローカルに保存すること
-	Commit してもまだ GitHub にはアップロードされていない


### 4. Push して GitHub に反映させる
-	右上の [Push origin] をクリックします
-	"Push completed successfully" と表示されます（Pushできました！）
-	GitHub の Web ページでリポジトリを開き、変更が反映されたことを確認します

✔ ポイント
-	Push はローカルの変更を GitHub にアップロードすること
-	他のメンバーもこの変更をみることができるので、以降共同での作業が可能となる


### 5. Pull してローカルを最新状態に保つ
-	右上の [Fetch origin] をクリック（最新の変更があるか確認）します
-	There are updates available と表示されたら [Pull origin] をクリックします
-	"Pull completed successfully"と表示されます（同期できました！）

✔ ポイント
-   Pull は最新（自分の別のローカルマシーンでの作業、共同メンバーの作業）の状態に更新するボタンと考えてよい
-   Pull せずに作業すると、古い状態で編集してしまうリスクがある
-   Push の前に Pull する習慣をつける（Pull → Edit → Commit → Push）