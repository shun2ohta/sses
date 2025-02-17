## GitHub Desktop を使って履歴管理を行う［基本編］

公開: 2025-02-16 17:05:10


GitHub Desktop というアプリケーションがあり、これでもリポジトリの履歴を管理することができます。具体的には、「History」タブを見ると、どんな変更をしたのかふりかえることが可能で、メニューから選んだり、右クリック（ダブルタップ）して、やりたいことを選ぶだけです。このドキュメントは、<ins>リポジトリを作成し、main に Commit、Push、Pull をして最新状態に保つまで</ins>を扱うためにあります。

なお、GitHub Desktop というときには、アプリケーションのことを指し、単に GitHub というときには、Web 版の リモートの GitHub 本体のことを指します。


### 0. 事前に行うこと
-   GitHub の [アカウントを作成](https://docs.github.com/ja/get-started/start-your-journey/creating-an-account-on-github) します
-   GitHub にログインし、[新規にリポジトリを作成](https://docs.github.com/ja/repositories/creating-and-managing-repositories/creating-a-new-repository)します
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

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Clone_a_Repository.png" alt="Clone_a_Repository" width="45%">
    </div>

    **図1. リポジトリのクローンをつくる**　自分で作成したリポジトリや招待されたリポジトリのみクローンをつくることができます。
    <br><br>

**✔ ポイント**
-	クローンとは GitHub 上のリポジトリ（リモートリポジトリと呼びます）を 自分のマシン（ローカル）にコピーすること
-	ローカルで作業した内容がリモートリポジトリに反映されるようになる
<br><br>

### 2. クローンしたローカルディレクトリに変更を加える
-   何かファイルをクローンしたローカルディレクトリに置いてみます
-	適当なファイルを　CotEditor や VSCode などで編集してみます（他のアプリケーションを使うときと同様に、適宜保存してください）

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Finder_OpenFile.png" alt="Finder_OpenFile" width="50%">
    </div>

    **図2. ローカルディレクトリでで編集作業を行う**　Finderでファイルを新たに置いたり（この例では、svgファイル）、編集したりすることができます。README.md を開くと次の図3のようになります。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/EditingFile.png" alt="EditingFile" width="50%">
    </div>

    **図3. VSCodeのエディタで編集作業を行う**　エディタは好みのものでよく、これに限りません。この例では、README.md に1行追記しています。
    <br><br>

**✔ ポイント**
-	編集作業そのものを必ずローカルディレクトリのなかで行う
-	4番以降を実行するまでは変更過程を他の誰もみることはできないので安心してよい
<br><br>

### 3. Commit する
-	GitHub Desktop を開きます → 変更が検出されています
-	Summary 欄に変更内容を説明するメッセージを入力（例: 東京の気候値を追加）します
-	[Commit to main] をクリックします

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/List_of_Changes.png" alt="List_of_Changes" width="50%">
    </div>

    **図4. ローカルディレクトリの変更は即座に検知される**　作業をローカルディレクトリで行うと、どんな変更を行なったかを自動的にリスト表示してくれます。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Summary_Commit2main.png" alt="Summary_Commit2main" width="30%">
    </div>

    **図5. main に Commit する**　Summary にはごく簡単に何を変更したかがわかるように記します（日本語でも構いません）。すると、Commit to main のボタンを押すことができるようになります。
    <br><br>

**✔ ポイント**
-	Commit は変更内容をローカルに保存すること
-	Commit してもまだ GitHub にはアップロードされていない
<br><br>


### 4. Push して GitHub に反映させる
-	右上の [Push origin] をクリックします
-	"Push completed successfully" と表示されます（Pushできました！）
-	GitHub の Web ページでリポジトリを開き、変更が反映されたことを確認します（図7）
-   GitHub Desktop の場合、History タブをみると、同様に変更が反映されていることがわかります（図8）

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Push_Undo.png" alt="Push_Undo" width="80%">
    </div>

    **図6. Commit の内容を Push する**　Commit に問題がなければ、Push origin を押して、main に反映させます。Commit の内容を修正したい場合には Undo ボタンを押します。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/ConfirmRemoteRepo1.png" alt="ConfirmRemoteRepo1" width="70%">
    </div>

    **図7. main に Push されたかを確認する1**　GitHub 上を確認（ブラウザをReload）すると、Mac の Finder 上の操作結果が反映されていることがわかります。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/ConfirmRemoteRepo2.png" alt="ConfirmRemoteRepo2" width="70%">
    </div>

    **図8. main に Push されたかを確認する2**　GitHub Desktop の Histroy タブ　で確認できる履歴をクリックすると、右側にどのような変更が加わったかを知ることができます。慣れると、ブラウザを使わず、GitHub Desktop のみで確認できるようになります。
    <br><br>

**✔ ポイント**
-	Push はローカルの変更を GitHub にアップロードすること
-	他のメンバーもこの変更をみることができるので、以降共同での作業が可能となる
<br><br>


### 5. Pull してローカルを最新状態に保つ
-   自身あるいは共同メンバーがファイルを更新したり、追加、削除を行うと、自動でリストとともに、 [Pull origin] ボタンが表示されているはずです
-	最新の変更があるかわからない場合には、右上の [Fetch origin] をクリックします
-	変更がなければそのまま、変更があれば [Pull origin] が表示されているので、これをクリックします
-	"Pull completed successfully"と表示されます（同期できました！）
-   同期したファイルを確認します

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Pull_origin.png" alt="Pull_origin" width="70%">
    </div>

    **図9. main に 変更があると自動的に Pull するように促される**　リモートリポジトリに変更があるので、まずはローカルにも同期をとり、その後、履歴を確認します（次の図10）。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Fetch_origin.png" alt="Fetch_origin" width="30%">
    </div>

    **図10. 手動でリモートリポジトリに変更があるか確認する**　リモートリポジトリに変更があるかどうかわからない場合、Fecth することで、Pull する必要があるかないかがわかります。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/ConfirmRemoteRepo3.png" alt="ConfirmRemoteRepo3" width="60%">
    </div>

    **図11. リモートリポジトリの変更をローカルにも反映させる**　ローカルに Pull することで、リモートリポジトリにどのような変更があったかを知ることができます。この例では、README.md に（図8と比較すると）さらに1行追加されていたということがわかります。
    <br><br>

**✔ ポイント**
-   Pull は最新（自分の別のローカルマシーンでの作業、共同メンバーの作業）の状態に更新するボタンと考えてよい
-   Pull せずに作業すると、古い状態で編集してしまうリスクがある
-   Push の前に Pull する習慣をつける（Pull → Edit → Commit → Push）
