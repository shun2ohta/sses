## GitHub Desktop を使って Commit を整理する［Squash］

公開: 2025-02-17 21:28:44


ある程度 GitHub で Commit → Push を繰り返していると、Commit を統合したくなることが出てくるでしょう。とくに多いのが、Commit した直後に「これも直しておくべきだった」と追加したいということです。その度に Commit をし続けると、細か過ぎる Commits が大量に溜まり、履歴管理という点では望ましくない（あとから確認したいときに大変になります）です。大事な点ですが、そんなときには、Push を避けることです。ここでは、**Push 前の複数の Commits を統合（Squash）する** 流れをみていきましょう。


### 1. 統合したい Commits を確認する
-	GitHub Desktop を開きます
-	統合したい Commit を一つずつ選択して、変更点を確認します（**図1**）
-	もう一つの統合したい Commit も選択して、変更点を確認します（**図2**）
-   軽微な修正ごとに Commit するより、まとめて一つにしても（同一水準の修正で同じグループであるので）問題なく、そのほうがのちの履歴管理が楽になると判断できます

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Commit1.png" alt="Commit1" width="80%">
    </div>

    **図1. Commit を確認する1**　21行目に一語だけ追記されていることがわかります。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Commit2.png" alt="Commit2" width="80%">
    </div>

    **図2. Commit を確認する2**　22行目の一文が変更されていることがわかります。
    <br><br>


**✔ ポイント**
-	他の協調作業者にも迷惑がかからないので、Push 前（Commit の段階）に統合するほうがよい
-	のちに履歴を管理することを想定して Commit を行うほうがよい
<br><br>


### 2. 細か過ぎる Commits を Squash する
-	統合したい Commits を2つ選択して、変更点を確認します（**図3**）
-	そのまま右クリック（ダブルタップ）をして「Squash 2 Commits...」を選びます（**図3**）
-   軽微な修正ごとに Commit するより、まとめて一つにするほうがのちに楽になると判断できます
-   自動で補完されますが、Summary と Description をわかりやすいものに変更するとよいでしょう（**図4**）
-   「Squash 2 Commits」を押します

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Squash2Commits.png" alt="Squash2Commits" width="80%">
    </div>

    **図3. Commits を選び、右クリック（ダブルタップ）する**　21〜22行目の変更がまとめて表示されています。図1〜2の内容がまとめられていることがわかります。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Summary-Description.png" alt="Summary-Description" width="45%">
    </div>

    **図4. Summary と Description に Commit メッセージを書く**　デフォルトでそれぞれの Commit メッセージから補完されますが、必要に応じてわかりやすい Commit メッセージに修正するとよいでしょう。
    <br><br>


**✔ ポイント**
-	複数回の Commits があたかも1回の Commit をしたように整理される
<br><br>


### 3. Squash された Commit を確認し、Push する
-	統合した Commit を選択すると、統合された変更点を確認できます（**図5**）
-	2つの細かい Commits が1つになりました（**図5**）
-   Push して、リモートリポジトリに変更点を反映させます

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/SuccessfullySquashed.png" alt="SuccessfullySquashed" width="80%">
    </div>

    **図5. 統合した Commit を選び、確認する**　図3と同じ変更内容になっていて、1つの Commit にまとめられていることがわかります。
    <br><br>

**✔ ポイント**
-	最後に Push することを忘れないこと
<br><br>


### ■ なぜ Push 後の Commit の統合は勧められないのか？

Push 後であっても、自身のリポジトリであり、かつ他の招待したユーザーがまだ参照していない場合（Push の直後など）には、Commit の整理をしても問題はありません。もっともよくあるシチュエーションは、自分一人のための履歴管理の場合です。そうではなく、グループでの共同作業を目的としたリポジトリの場合には、Push 後に Commit の整理をするには注意が必要です。


### ■ Push 後に Commit の統合を行う
-   図3と同様に、統合したい Push した Commit を複数選択し、Squash を実行します
-   すると、統合するには Force Push が必要になるが、始めてもよいか？と尋ねられます → 「Begin Squash」を押します（**図6**）
-   「Force push」を実行します（**図7**）
-   Force Push を実行すると main の履歴も書き換えられ、共同作業をしているブランチと不整合が起きるよ、という最終確認があり、「I'm sure」を選びます（**図8**）

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/BeginSquash.png" alt="BeginSquash" width="70%">
    </div>

    **図6. Force Push をともなう Squash であることを確認される**　アラートが出ている間に、共同作業をしている人はいないかなど、確認をするとよいでしょう。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/ForcePush_origin.png" alt="ForcePush_origin" width="40%">
    </div>

    **図7. Force Push を実行する**　通常の Push と同様に操作します。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/ForcePush.png" alt="ForcePush" width="70%">
    </div>

    **図8. Force Push を実行する直前に最終確認を求められる**　繰り返しアラートが出るうちの最後のものです。それくらい、Force Push は状況によっては副作用があることを理解しておきましょう。
    <br><br>

**✔ ポイント**
-	ある程度、履歴管理に慣れるまでは、Squash は Push 前の Commit に限定して実行するとよい
<br><br>
