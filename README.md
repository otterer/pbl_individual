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
## 実行方法
```
python src/copybot_pdf.py
```
* 上記を実行した上で、BotをインストールしたSlackチャンネルで「PDF」を含むメッセージを投稿するとBotが起動する。
* ストリーミングモードの有無を選択した上でPDFファイルを投稿する。
* 処理完了の旨をBotが回答したら、PDFに関する任意の質問やタスク指示を投稿する（その際、`質問だよ`or`聞くね`を文頭に書く。）
* PDFから質問やタスク指示と関連するページを探索し、その情報に基づきBotが回答してくれる。

## チケット
[PB2](https://www.notion.so/PBL-2023-5-Bot-Notion-2023-5-b10b1ab8a284449f890b719231737e4f?pvs=4) or [PB4](https://www.notion.so/AIIT-Q-Q-Q-bot-0e69ebd6f0b540fe9563dc3f32d352ee?pvs=4)（に関連する一部機能）

## やったこと
後々のバックログにモブプロで取り組むとき用の実装サンプルを作成しました。
#8 では週報データベースという限られたデータ形式からのみ情報取得する形でしたが、これ以外の幅広いNotionドキュメントに対してもスコープを拡げるため、PDF形式でエクスポートした任意のNotionページに対して以下の処理を行う機能を実装しました。

1. Slackに投稿されたPDFファイルをSlackAPIを使って取得
2. 取得したPDFからページ単位でテキスト抽出
3. 抽出したテキストをベクトルデータ化
    - OpenAI APIの`get_embedding`関数によりベクトル変換
    - ページ単位でチャンキングし、１ページ１レコードのPandas.DataFrameを作成
4. PDFについてユーザーがSlackに投稿した文章（質問やタスク指示）もベクトル変換し、これに関連する上位３ページのテキスト（ベクトル）をコサイン類似度により抽出
5. ユーザー投稿文と上位３ページのテキストを使ってプロンプトをつくり、ChatGPTに入力してその回答をSlackに投稿

## できるようになること（ユーザ目線）
* PDF形式でエクスポートした任意のNotionページをSlackに投稿するだけで、そのドキュメントに関することなら何でもBotが答えてくれる。要約や振り返り素案の作成もしてくれる。

## ストリーミングモードについて
#8 で実装した機能です。プルダウンでストリーミングモードを選択するとChatGPTが回答文を生成する際、全文の生成完了を待たずに、100 tokens 生成するたびに逐次Slackに投稿を行います。Botからの応答時間が長くなることによるユーザーの違和感を軽減するための機能です。

## 動作イメージ
![image](https://github.com/yellow-seed/slack_bolt_sample/assets/82159549/934034a4-8df8-46b1-b42d-c446668ffc83)


# Markdownファイルの要約
```
python src/copybot_md.py
```
* `マークダウン`を含む文言をSlackチャンネルに投稿する。
* Botから返答があったら、Notionからエクスポートしたマークダウンファイルを投稿する。
* Botが要約してくれる。

![image](https://github.com/yellow-seed/slack_bolt_sample/assets/82159549/aed3c88c-bd96-4df9-b3df-a8e295486c54)
