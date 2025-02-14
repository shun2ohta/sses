## Google Colaboratory の Jupyter Notebook を GitHub で管理する

公開: 2024-11-24 12:12:18（更新: 2025-02-10 20:17:00）



Pythonを使った処理を行う場合、Google Colaboratory（Colab）は驚くほど高機能で、何もしなくてもどんどんアップデートしてくれるので、授業教材だけでなく、研究でも多くの局面で利用できます。高機能と書きましたが、履歴機能も充実しています。過去のヴァージョンにいつでも戻って実行が行えるほか、Colab 内での保存のたびに GitHub でいう Commit が行われているといって差し支えないです。つまり、通常の Colab ファイルの編集を行なっていれば、ヴァージョン管理を意識する必要がないのです（Apple の Keynote や Pages などと同じです）。ただし、一人のユーザーで処理が完了する場合には、という限定がつきます。数人で共同する場合、Google Drive で Colab ファイルの共有を許可しておけば、書き込み権のあるユーザーと共同編集はできます。いつ誰が書いたかは「ファイル」－「変更履歴」で差分を見ることでわかります。またコメント機能もあるので、コメントを残すことで申し送りをすることも可能でしょう。

ただし、GitHub が持つ細やかで柔軟なヴァージョン管理機能を利用したい、共同でコードの管理、開発、編集を積極的に行いたい、という場合には、Colab が持つ GitHub 連携の機能を使います。当然ですが、すでに GitHub のアカウントを持ち、連携すべきリポジトリやブランチを管理できていることが前提です。

### 1. Colab のファイルを GitHub 連携する

Colab で作成した（あるいは作成途中の）Jupyter Notebook を GitHub 連携するには、「ファイル」－「GitHubにコピーを保存」を選びます。Commit 画面が表示されるので、対象とするリポジトリとブランチを指定し、Commit Comment を書いて OK を押します。これで GitHub でいう Push が実行されます。ウェブなどの情報の多くもここで止まっています。これだけであれば、単に GitHub にバックアップを置いているだけに等しく、メリットを感じることがほとんどありません。

GitHub連携をしたファイルに保存をします。通常の「ドライブにコピー」ではなく、ファイル名の横に表示されている「変更内容を保持するには GitHub に保存してください」という指示に従います。しかしながら、そのようなメニューはありません。通常の「ファイル」－「保存」を選ぶか、Command＋S を実行します。あるいは「変更内容を保持するには GitHub に保存してください」という部分をクリックします。

<div style="text-align: center;">
  <img src="https://www.gesw.org/img/memo/SaveColabFile2GitHub.png" alt="Save a Colab File in GitHub" width="50%">
</div>

すると、次のようなポップアップメニューが出てきますので、Commit Comment を書いて、Push します。

<div style="text-align: center;">
  <img src="https://www.gesw.org/img/memo/Colab2GitHub.png" alt="Connection between Colab and GitHub" width="50%">
</div>

自動保存はできません。ただし、頻繁に保存を行うとそのたびに Commit → Push が行われてしまいます。履歴管理の面であまり複雑にしたくないということと書いたものをこまめに保存したいということが両立しません。それだけでなく、毎回保存した GitHub 上のファイルを新規のタブとして開いてくれてしまいます。煩わしく感じます。


### 2. GitHub 連携した Colab ファイルを VSCode で編集する

細かすぎる Commit を整理したり、誤りを廃棄したりするなどの作業はローカルにクローンを作成するほうがよいでしょう。

GitHub Desktop などでローカルにクローンを作成します。VSCodeでそのディレクトリを開き、Jupyter Notebook をそのまま編集しても構いません。あるいは、「Open in Colab」のボタンをクリックして Google Colab で編集してもよいです。ファイルの入出力があるような Notebook では互換性がないので、実行は Colab で行うこととし、VSCode ではそれ以外の編集や実行を行うとスマートでしょう。対象のディレクトリにTerminalでも移動すれば、`git reset` や Commit、ファイルの追加など一連の作業ができるようになります。

似たようなことを考えている人はあちこちにいらっしゃるようです。→
[5. Google colab, GitHub, VSCodeの連携](https://programmingforever.hatenablog.com/entry/2024/08/01/131311)

