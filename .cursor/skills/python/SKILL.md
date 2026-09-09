---
name: python
description: >-
  Explains basic Python syntax used in the user's code, and reviews/fixes code
  against the Google Python Style Guide. Use when the user invokes /python, asks
  for Python grammar explanation, or requests Google style review/correction.
disable-model-invocation: true
---

# Python（文法解説 + Google Style）

対象コードを読み、次の2つを行う。

1. **コードに使われている Python の基本的な文法の解説**
2. **[Google Python Style Guide](https://chromium.googlesource.com/external/github.com/google/styleguide/+/f9347e1e9d79aee9cde0802fe178d72c8f87926c/pyguide.md) による適切なコーディングかどうかの判定・修正**

詳細ルールは [style-checklist.md](style-checklist.md) を参照する。迷ったら公式ガイドを優先する。

## 対象の決め方

1. ユーザーがファイル・範囲を指定 → それを使う
2. 未指定 → 開いているファイル / 直近の会話のコード / 選択範囲
3. 対象が不明なら、どのファイルか確認してから進む

## ワークフロー

### 1. 文法解説

- **そのコードに実際に出てくる構文だけ**を解説する（使っていない機能は説明しない）
- 初心者向けに、日本語で簡潔に書く
- 各項目は次の形にする:
  - **構文名**（例: `for` / リスト内包表記 / `yield`）
  - このコードでの意味（1〜2文）
  - 必要なら短い例（当該コードの抜粋で十分）
- アルゴリズムの正しさの講義はしない（聞かれたときだけ）

### 2. Style Guide 判定

[style-checklist.md](style-checklist.md) に沿って点検する。

- 違反ごとに: 箇所（行 or 抜粋） / 該当ルール / なぜ問題か / 修正案
- 問題なしの項目は長々と書かない
- 学習用の短いスクリプトでは、docstring・型注釈・`main()` は **提案** にとどめ、強制しない（ユーザーが修正を求めたら適用）

### 3. 修正

- ユーザーが修正を求めた、または「判定・修正」と指示したときだけファイルを編集する
- 解説のみのときはコードを変えない
- 修正時は振る舞いを変えず、Style 違反の解消に限定する
- 大きな書き換えの前に、変更方針を一文で示す

## 出力フォーマット

日本語で、次の構成にする:

```markdown
## 文法解説
- **構文**: …
- **構文**: …

## Style 判定
- ✅ おおむね適合 / ⚠️ 要修正あり
- （違反があれば箇条書き）

## 修正案
（修正する場合のみ。差分の要点 or 修正後コード）
```

ユーザーが片方だけ求めたときは、そのセクションだけ出す。

## 注意

- Style Guide と学習目的がぶつかる場合（例: 書籍のサンプルに合わせた命名）は、違反として指摘したうえで「学習用として残す / Style に直す」を選べるようにする
- 秘密情報や無関係ファイルには触れない
