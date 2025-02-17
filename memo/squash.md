## GitHub Desktop を使って Commit を整理する［Squash］

公開: 2025-02-17 21:28:44


ある程度 GitHub で Commit → Push を繰り返していると、Commit を統合したくなることが出てくるでしょう。とくに多いのが、Commit した直後に「これも直しておくべきだった」と追加したいということです。その度に Commit をし続けると、細か過ぎる Commits が大量に溜まり、履歴管理という点では望ましくない（あとから確認したいときに大変になります）です。大事な点ですが、そんなときには、Push を避けることです。ここでは、**Push 前の複数の Commits を統合する（Squash する）** 流れをみていきましょう。


### 1. 統合したい Commits を確認する
-	GitHub Desktop を開きます
-	統合したい Commit を一つずつ選択して、変更点を確認します（**図1**）
-	もう一つの統合したい Commit も選択して、変更点を確認します（**図2**）
-   軽微な修正ごとに Commit するより、まとめて一つにするほうがのちに楽になると判断できます

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
-   自動で補完される Summary と Description をわかりやすいものに変更するとよいでしょう（**図4**）
-   「Squash 2 Commits」を押す

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Squash2Commits.png" alt="Squash2Commits" width="80%">
    </div>

    **図3. Commits を選び、右クリック（ダブルタップ）する**　21〜22行目の変更がまとめて表示されています。図1〜2の内容がまとめられていることがわかります。

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/Summary-Description.png" alt="Summary-Description" width="45%">
    </div>

    **図4. Summary と Description に Commits メッセージを書く**　デフォルトでそれぞれの Commit メッセージから補完されますが、必要に応じてわかりやすい Commits メッセージに修正するとよいでしょう。
    <br><br>


**✔ ポイント**
-	複数回の Commits があたかも1回の Commit をしたように整理される
<br><br>


### 3. Squash された Commit を確認する
-	統合した Commit を選択すると、統合された変更点を確認できます（**図5**）
-	2つの細かい Commits が1つになりました（**図5**）

    <br>
    <div style="text-align: center;">
    <img src="https://www.gesw.org/img/memo/SuccessfullySquashed.png" alt="SuccessfullySquashed" width="80%">
    </div>

    **図5. 統合した Commit を選び、確認する**　図3と同じ変更内容になっていて、1つの Commit にまとめられていることがわかります。

