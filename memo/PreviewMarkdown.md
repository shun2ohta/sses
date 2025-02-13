## VSCode でプレビューしながらマークダウン記法の書類を編集する

公開: 2025-02-10 21:29:11



マークダウン記法の書類は好みのエディタで作成すればよいですが、都合のよいプレビュー機能のあるツールはそれほど多くありません。VSCodeでも編集するシチュエーションは多く、VSCode内で簡単なプレビューができるとよいでしょう。何もインストールしなくても、VSCodeでマークダウン記法の書類を開いている状態で、エディタのスプリットヴューのアイコンをクリックすると、左右に分割され、左がコード（編集画面）、右にプレビュー画面が表示されます。

<div style="text-align: center;">
  <img src="https://www.gesw.org/img/memo/Preview_Icon.png" alt="Preview markdown icon" width="50%">
</div>


ただ表示するだけであれば、この標準機能で十分で、マークダウンを書きながら右画面でプレビューで確認できます。

さらに、CSSを工夫したり、PDFに出力したりなどする場合には機能拡張をインストールすると簡単に実現できます。今回は [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/ja-jp/) をインストールしてみました。好みに応じて、いろいろ試してみるとよいでしょう。

VSCodeではなく、Macのエディタ（CotEditorを愛用しています）でマークダウンの書類を作成している場合には、Chromeの拡張機能である [Markdown Viewer](https://github.com/simov/markdown-viewer) がよさそうです。次のような記事も参考になりそうです→[Chrome拡張機能「Markdown Viewer」でmarkdownをいい感じに表示する](https://qiita.com/takachan_coding/items/7a0978a70208e482aae9)。