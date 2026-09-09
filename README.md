## Step1

- 答えを見ずに菅んが得て、5分考えてわからなかったら答えを見る
- 答えを見て理解したら答えを隠して書く
- また5分迷ったら答えを見る
- 見たら全て消してやりなおす
- 答えを送信して正解になればStep1は完了

## Step2

- Step1のコードを読みやすくなるようにできるだけ整える
- 過去に同じ問題を解いた人のコードを読む
- これで動くようになればStep2はOK

## Step3
- 他の回答方法はないかを検討、検索をする

## Step4
- レビューを踏まえて整形する。その後、10分以内にエラーを出さずに書く

## standalone

各問題フォルダ内の `standalone/` は、**検証専用** の場所
ルート直下の `step1.py` / `step2.py` などは練習・提出用のコードとして書き、`standalone/` ではそれを import して動作確認や計測を行う

## dsa

[新・明解Pythonで学ぶアルゴリズムとデータ構造 第２版](https://www.bohyoh.com/Books/NewMeikaiPythonAlgorithm_2nd/index.html) を読みながら、実際にコーディングするためのフォルダ。


### フォルダ構成（例）

プロジェクト内の standalone 構成を確認し、README 用の文案を用意します。

会話の流れとこれまでの構成から、README.md に足す standalone セクション の文案案です。既存の Step1〜4 の後に追加する形を想定しています。

## standalone
各問題フォルダ内の `standalone/` は、**検証専用** の場所です。  
ルート直下の `step1.py` / `step2.py` などは練習・提出用のコードとして書き、`standalone/` ではそれを import して動作確認や計測だけを行います。
### フォルダ構成（例）
```
9_Palindrome_Number/
├── step1.py # 解答
├── step2.py 
├── memo.md # 考察・実行結果のメモ 
└── standalone/ 
├── bench.py # 検証用の共通関数（実行時間計測など） 
└── step.py # import して実行するだけ（または step1.py / step2.py）
```