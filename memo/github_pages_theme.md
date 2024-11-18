## GitHub Pages の体裁を整える

GitHub Pagesでは、`README.md` が自動で `index.html` に変換されて公開されるように、設定後は、マークダウンで適当にマークダウンのファイル（下の例では、`memo/{1-xxx.md, 2-xxx.md）を置くと、数秒後にはHTMLに変換されて公開されます。

.
├── README.md（index.md）
├── _config.yml
├── _layouts
│   └── default.html（公式サイトからコピーして変更）
├── assets
│   └── css
│       └── style.scss
├── img
│   └── favicon.jpg
└── memo
　   └── 1-×××.md
　   └── 2-×××.md

さらに、いくつかの設定ファイルを置くことでウェブサイトの見た目を変更することができます。


### _config.yml

公式のペイジにある推奨テーマは下記の1行を書くだけでCSS等が一括で反映されます。
```
theme: jekyll-theme-cayman
```



### _layouts/default.html



