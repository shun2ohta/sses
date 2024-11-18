## GitHub Pages で公開するペイジの体裁を整える

GitHub Pagesでは、`README.md` が自動で `index.html` に変換されて公開されるように、GitHub Pagesの設定後は、適当にマークダウンのファイル（下の例では、`memo/{1-xxx.md, 2-xxx.md}`）を置くと、数秒後にはHTMLに変換されて公開されます。

```
./
├── README.md（→index.html に変換される）
├── _config.yml
├── _layouts
│   └── default.html（公式サイトからコピーして変更）
├── assets
│   └── css
│       └── style.scss（スタイルシートの最初の4行は公式サイトからコピーする）
├── img
│   └── favicon.jpg（必要ならば）
└── memo
　   ├── 1-×××.md（→1-×××.html に変換される）
　   └── 2-×××.md（→2-×××.html に変換される）
```

さらに、いくつかの設定ファイルを置くことでウェブサイトの見た目を変更することができます。変更したいものだけ変更すれば、デフォルトから上書きされます。


### _config.yml

[公式のペイジにある推奨テーマ](https://pages.github.com/themes/) を使う場合、下記の1行を書くだけでCSS等が一括で反映されます。この例では、[cayman](https://github.com/pages-themes/cayman)というテーマを使っています。
```
theme: jekyll-theme-cayman
```
ほかに、`title`と`description`を設定することもできます。各マークダウンファイルから生成されるhtmlファイルに自動で埋め込まれます。
```
title: "早大人間環境・太田俊二"
description: "太田俊二（早大人間環境）:　雑多な記録"
```
ちなみに、[caymanのデフォルトの見た目は公式サイト](https://pages-themes.github.io/cayman/)をご覧ください。ほかに[サポートされているテーマは公式サイト](https://pages.github.com/themes/)の一覧のペイジにあります。[カスタマイズの方法は公式サイトにも記されて](https://github.com/pages-themes/cayman?tab=readme-ov-file#customizing)います。


### _layouts/default.html

[caymanの公式サイト](https://github.com/pages-themes/cayman)から、`_layouts/default.html`をコピーして必要のない行などを削除します。
- デフォルトの header が重たいので、GitHubのソースを参照する箇所を削除しました。
- デフォルトの footer にもGitHubのソースを参照する箇所があるので削除しました。


### assets/css/style.scss

[caymanの公式サイト](https://github.com/pages-themes/cayman)から、`assets/css/style.scss`をコピーして（最初の4行のみが記されている）、続けてスタイルシートを作成します。headerを中心に独自色を出してみます（色や余白の設定をデフォルトから変更しています）。
```
.page-header{
    background-image:linear-gradient(to right, #d55d64 0%, #e49129 50%, #c0671c 100%);
    text-align: center; /* 中央揃えを維持 */
    padding-top: 15px; /* 上部余白 */
    padding-bottom: 5px; /* 下部余白を同じ値にすると下部余白が広くなる（フォントのせい？） */
    margin: 0 auto; /* 中央配置を維持 */
    height: auto;  /* 必要に応じて高さを自動調整, height: 50px; と指定してもよい*/ 
};
```


