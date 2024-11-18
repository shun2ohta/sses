## GitHub Pages で公開するペイジの体裁を整える

GitHub Pagesでは、`README.md` が自動で `index.html` に変換されて公開されるように、GitHub Pagesの設定後は、適当にマークダウンのファイル（下の例では、`memo/{1-xxx.md, 2-xxx.md}`）を置くと、数秒後にはHTMLに変換されて公開されます。

```
.
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
　   └── 1-×××.md（→1-×××.html に変換される）
　   └── 2-×××.md（→2-×××.html に変換される）
```

さらに、いくつかの設定ファイルを置くことでウェブサイトの見た目を変更することができます。


### _config.yml

公式のペイジにある推奨テーマは下記の1行を書くだけでCSS等が一括で反映されます。この例では、caymanというテーマを使っています。
```
theme: jekyll-theme-cayman
```
ほかに、`title`と`description`を設定することもできます。各マークダウンファイルから生成されるhtmlファイルに自動で埋め込まれます。
```
title: "早大人間環境・太田俊二"
description: "太田俊二（早大人間環境）:　雑多な記録"
```
ちなみに、[caymanのデフォルトの見た目は公式サイト](https://github.com/pages-themes/cayman)をご覧ください。ほかに[サポートされているテーマは公式サイト](https://pages.github.com/themes/)の一覧のペイジにあります。



### _layouts/default.html



