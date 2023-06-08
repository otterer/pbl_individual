# 前提
* VSCodeの拡張機能"Dev Containers"のインストール
* Docker Desktopのインストールと起動
* 上記が済んだ状態でVSCodeのReopen in Containerを実行
* .env.example を.env にファイル名変更し、必要なAPI KEYを指定
* Slackアプリはソケットモードに設定しておく
* Slackアプリの必要権限
  * App-Levelのスコープ：`connections:write`
  * Bot-Levelのスコープ：`chat:write`, `files:read`

# 週報の取得と要約

```
python src/copybot.py
```
* 上記を実行した上で、BotをインストールしたSlackチャンネルで「週報要約」または「マンスリーレビュー」を含むメッセージを投稿するとBotが起動する。
* `ストリーミングモード`の適用有無と`対象月`をプルダウンで選択すると、BotがNotionの週報まとめページから対象月の全メンバーの週報を取得し、１か月分の内容を要約して回答する。
* ストリーミングモードを選択した場合にはChatGPTが回答を作成する際、全文の生成完了を待たずに100tokens 生成するたびにSlackに順次回答を投稿する。

![image](https://github.com/otterer/PBL/assets/82159549/47590a08-fa50-4b41-8918-4e003390cb5a)


# PDFに基づく回答
```
python src/copybot_pdf.py
```
* 上記を実行した上で、BotをインストールしたSlackチャンネルで「PDF」を含むメッセージを投稿するとBotが起動する。
* ストリーミングモードの有無を選択した上でPDFファイルを投稿する。
* 処理完了の旨をBotが回答したら、PDFに関する任意の質問やタスク指示を投稿する（その際、`質問だよ`or`聞くね`を文頭に書く。）
* PDFから質問やタスク指示と関連するページを探索し、その情報に基づきBotが回答してくれる。

![image](https://github.com/otterer/pbl_individual/assets/82159549/4fd12601-ba78-4f1e-82ac-c91ac4922971)


# Markdownファイルの要約
```
python src/copybot_md.py
```
* `マークダウン`を含む文言をSlackチャンネルに投稿する。
* Botから返答があったら、Notionからエクスポートしたマークダウンファイルを投稿する。
* Botが要約してくれる。
