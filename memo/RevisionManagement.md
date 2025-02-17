## GitHub Desktop を使って履歴管理を行う［ブランチ編］

公開: 2025-02-12 10:31:44


GitHub Desktop というアプリケーションがあり、これでもリポジトリの履歴を管理することができます。具体的には、「History」タブを見ると、どんな変更をしたのかふりかえることが可能で、メニューから、あるいは右クリック（ダブルタップ）して、やりたいことを選ぶだけです。このドキュメントは、すでに<ins>リポジトリを作成し、main に Commit、Push までを行ったことがある</ins>人が次の段階に進むためにあります。

GitHub Desktop を使えばコマンドを覚えなくても直感的に操作でき、**基本的なブランチ管理から Pull Request 作成まで**といった一連の過程も実現できます。慣れてくると、GUI はいちいち面倒で、煩わしく感じてくるものですが、まずは GitHub Desktop を使うことをお勧めします。以下の手順の概略を実践しながら理解するとよいです。

なお、GitHub Desktop というときには、アプリケーションのことを指し、単に GitHub というときには、Web 版の リモートの GitHub 本体のことを指します。


### 1. ブランチを作成します
-	GitHub Desktop を開きます
-	左上のブランチメニューをクリック → 「New Branch…」を選択します（**図1**）
-	ブランチ名を入力して、「Create Branch」を押します（**図2**）

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/New_Branch.png" alt="New_Branch" width="40%">
	</div>

	**図1. ブランチをつくる準備**　Current Branch,　main とある部分をクリックして、New Branch ボタンを押します。

	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/Create_a_Branch.png" alt="Create_a_Branch" width="40%">
	</div>

	**図2. ブランチをつくる**　ブランチの性質をよく表すシンプルな名前をつけて Create Branch ボタンを押します。
	<br><br>


**✔ ポイント** － main から新しい作業ブランチをつくる（「ブランチを切る」と呼ぶことが多いです）ことで、main を直接変更せずに済みます。上記では、GitHub Desktop を使って作成していますが、もちろん GitHub の Web 版でも可能で、コマンドラインも含めて、複数の方法があります。
<br><br>


### 2. 変更を加えて Commit します
-	コードを編集（CotEditor, VSCode などで開く）します
-	GitHub Desktop に戻ると、変更が自動で検出されます
-	変更を確認し、「Summary」にコミットメッセージを入力します
-	「Commit to ブランチ名」をクリックします

**✔ ポイント** － Commit は「ローカル保存」なので、まだ GitHub には反映されていない状態です。
<br><br>


### 3. GitHub に Push します
-	上部の「Push Origin」ボタンをクリックします
-	GitHub にブランチがアップロードされます

**✔ ポイント** － Push すると、GitHub に変更が送信されますが、まだ main には反映されていません。
<br><br>


### 4. GitHub で Pull Request を作成します
-	GitHub Desktop の「Preview Pull Request」ボタンをクリックします（**図3**）
-	どのような変更がなされたかを確認することができます（**図4, 図5**）
-	GitHub Desktop の「Preview Pull Request」をプルダウンすると見える「Create Pull Request」ボタンをクリックします（**図6**）
-	すると、GitHub の Pull Request ページが開きますので、「Title」と「Description」を記入します（**図7**）
-	最後に「Create Pull Request」 をクリックします

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/PreviewPullRequest.png" alt="PreviewPullRequest" width="60%">
	</div>

	**図3. プルリクエストを準備する**　Create Pull Request ボタンを押します。

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/OpenPullRequest1.png" alt="OpenPullRequest1" width="60%">
	</div>

	**図4. 差分を確認する1**　いわゆる「間違い探し」と同じで、グラフィックスの変更の例（2-up）を示しています。変更の具合、度合いに応じて、比較方法を選べます。たとえば、一目で違いがわかりづらい場合には、Swipe を選び、左右にスワイプすることで小さな変化を確認しやすくなります。変更点を見比べて問題がないか確認をします。

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/OpenPullRequest2.png" alt="OpenPullRequest2" width="60%">
	</div>

	**図5. 差分を確認する2**　コードの変更例です。変更点を見比べて問題がないか確認をします。この例では、同じ38行目で `-` と `+` があるので、前者が変更前、後者が変更後を示しています。

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/PullDownMenu.png" alt="PullDownMenu" width="60%">
	</div>
	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/CreatePullRequest.png" alt="CreatePullRequest" width="60%">
	</div>

	**図6. プルダウンメニューを切り替える**　プレビュー（確認）が終わったら、「Create Pull Request」を行います。

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/Title_Desscription.png" alt="Title_Desscription" width="70%">
	</div>

	**図7. Pull Request に必須の項目を記入する**　何をどう変更したかを手短に記します。
	<br><br>

**✔ ポイント** － Pull Request をつくる（プルリクを送る、プルリクを出す、と呼ぶことが多いです）ことで、変更を安全にレビューしてから main にマージできます。
<br><br>


### 5. Pull Request をレビューして main にマージ（Merge）します
-	GitHub上で、変更を確認します
-	問題がなければ、「Merge pull request」をクリックします（**図8**）
-	すると、マージを行なってもよいかの確認（Confirm merge）を求められます（**図9**）
-	マージが完了し、Pull requestの処理も終わったので、Pull request が Close されます（**図10**）
-	「Delete branch」 を押して、使い終わったブランチを削除します

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/MergePullRequest.png" alt="MergePullRequest" width="60%">
	</div>

	**図8. GitHub 側でマージの確認を行う**　コンフリクトのチェックを自動で行い、問題がなければマージの準備が完了します。

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/ConfirmMerge.png" alt="ConfirmMerge" width="60%">
	</div>

	**図9. マージする内容を最終確認する**　Pull Requestの一連の処理が終了し、Close されたことを確認します。

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/PullRequestMerged_Closed.png" alt="PullRequestMerged_Closed" width="60%">
	</div>

	**図10. リモートリポジトリの main へのマージが完了する**　Closeされて、リモートリポジトリは更新されます。
	<br><br>


**✔ ポイント** － 用が済んだら、ブランチは捨てるほうがよいです。すでに main に取り込まれたブランチは不要なので、削除する方が管理しやすく、もし必要ならば、最新の main から新しいブランチを作成する方が安全で確実だからです（旧いブランチに最新のメインの状態を反映させることもできますが、ここでは省略します）。もちろん、当面の間、コミットする予定があるのであれば、ブランチを都度捨てる必要はありません。
<br><br>


### 6. ローカルの main を最新に更新します
-	GitHub Desktop に戻ります
-	左上のブランチメニューで main を選択 → 「Fetch origin」→「Pull origin」ボタン を押して最新の main を取得します（**図11**）
-	「History」からマージされているかを確認してもよいでしょう（**図12**）

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/PullOrigin.png" alt="PullOrigin" width="45%">
	</div>

	**図11. リモートリポジトリの main から Pull する**　これでローカルの main も完全に同期がとれました。

	<br>
	<div style="text-align: center;">
	<img src="https://www.gesw.org/img/memo/CheckHistory_main.png" alt="CheckHistory_main" width="70%">
	</div>

	**図12. ローカルリポジトリにマージが反映されているか確認する**　ローカルの main にもマージ内容が反映されていることがわかります。
	<br><br>

**✔ ポイント** － main が最新になっていることを確認し、新しい作業に進めます。
<br><br>




### ■ なぜブランチを切って更新し、その後 main にマージするのか？

直接 main に Push しない理由は大きく分けて3つほどあります。それぞれのポイントから説明していきましょう。

理由1: main を壊さないため
-	main は 安定したコードを保つ場所とします。
-	直接変更すると、バグが発生しても戻しにくいです。
-	開発用のブランチで作業すれば、問題が起きても main は安全です。

理由2: グループで作業しやすくするため
-	何人かが main を直接編集すると、変更が衝突しやすいです。
-	ブランチで分けて作業すれば、マージ前に調整できます。

理由3: 履歴をわかりやすく保つため
-	main に直接 Commit すると、履歴が複雑になりがちです。
-	ブランチを使うと「どんな作業をしていたか」明確に残ります。

**✔ ポイント1** － main に直接 Commit → Push すると、その時点で GitHub 上の main も更新されるので、Pull Request を出す必要はありません（GitHub Desktop でも「Pull Request」ボタンは現れません）。Pull Request は、ブランチの変更を main にマージするためのものなので、そもそも main に直接 Push すれば、マージしなくてもよいからです。しかしながら、共同で作業をする場合には、ブランチを切るべきです。「幹（main）」がいきなり更新されてしまうよりも、いったん「枝（branch）」が更新され、それを共同で確認（Review）し終わってから、マージされるほうが衝突（Conflict）が生じにくくなります。

**✔ ポイント2** － コード以外でも、リポートなどの添削をする場合がそうですが、ファイルを共同で編集することは多々あります。ゼミなどでその場で対応する場合には、いきなり main に Push するほうが（声をかけ合えばよいので）楽ですが、修正をする場合には、ブランチを切ってから Pull Request するのがよいでしょう。
