# 前提
* Visual Studio Codeの拡張機能"Dev Containers"のインストール
* Docker Desktopのインストールと起動
* 上が済んだ状態でVisual Studio CodeのReopen in Containerを実行すると、開発環境が起動し、Visual Studio Codeもその内部のファイルを編集できる状態になる
* .env.example を　.env にファイル名を変更し、SlackやOpenAIから取得したAPIキーなどの環境変数を入力する

# 実行方法
```
python main.py
```
上記を実行した上で、BotをインストールしたSlackチャンネルで「週報要約」または「マンスリーレビュー」を含むメッセージを投稿するとBotが起動する。
`ストリーミングモード`の適用有無と`対象月`をプルダウンで選択すると、BotがNotionの週報まとめページから対象月の全メンバーの週報を取得し、１か月分の内容を要約して回答する。

ストリーミングモードを選択した場合にはLLMが回答を作成する際、全文の生成完了を待たずに100tokens 生成するたびにSlackに順次回答を投稿する。

![image](https://github.com/otterer/PBL/assets/82159549/47590a08-fa50-4b41-8918-4e003390cb5a)
