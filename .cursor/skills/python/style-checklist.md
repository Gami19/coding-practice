# Google Python Style Guide — 判定用チェックリスト

出典: [Google Python Style Guide (commit f9347e1)](https://chromium.googlesource.com/external/github.com/google/styleguide/+/f9347e1e9d79aee9cde0802fe178d72c8f87926c/pyguide.md)

判定時はこの要約を使い、詳細・例外は公式ガイドを確認する。

## 言語ルール（要点）

| 項目 | 判定基準 |
|------|----------|
| Lint | `pylint` 想定。明らかな未使用・代入前参照などを指摘 |
| Imports | `import x` / `from x import y`。便利な別名は標準略称のみ（例: `np`）。フルパッケージ名を意識 |
| Exceptions | `raise MyError('msg')`。制御フローに例外を濫用しない。`assert` を本番の入力検証に使わない |
| Globals | 避ける。定数は `ALL_CAPS`。モジュール内なら `_name` |
| Nested | クロージャが必要なとき以外、隠す目的だけのネストは避ける |
| Comprehensions | 単純な1行のみ。複数 `for` / 複雑なフィルタは通常のループへ |
| Iterators | `for key in d:` / `if key not in d:` などデフォルトイテレータを使う |
| Generators | 利用可。docstring は `Yields:` |
| Lambda | 短い1行のみ。長いなら通常関数 |
| Conditional expr | 1行のときのみ。それ以外は `if` 文 |
| Default args | **可変オブジェクトをデフォルトにしない**（`[]` / `{}` 禁止）。`None` + 代入 |
| True/False | `if foo:` を優先。`None` は `is` / `is not`。空コンテナと `None` を混同しない |
| Power features | `hasattr` 乱用・メタクラス自作などは避ける（標準ライブラリ利用は可） |
| Types | プロジェクトに合わせて。公開 API は注釈を検討 |

## スタイルルール（要点）

| 項目 | 判定基準 |
|------|----------|
| Semicolons | 行末 `;` や同一行の複数文に `;` を使わない |
| Line length | **最大 80 文字**（URL や import の例外あり。公式参照） |
| Parentheses | 不要な括弧は付けない |
| Indentation | **スペース 4**。タブ禁止 |
| Blank lines | トップレベル定義のあいだは空行 2、メソッド間は 1 |
| Whitespace | 演算子・カンマまわりは通常のタイポグラフィに従う |
| Shebang | ほとんどの `.py` に不要。エントリポイントのみ検討 |
| Comments / Docstrings | モジュール・関数・クラスは適切な docstring。インラインは「なぜ」を書く |
| Classes | （ガイド記載どおり）基底なしなら `object` 継承を明示 ※Py3 では実質任意。指摘は軽め |
| Strings | 連結は判断で `+` / `%` / `format`。ガイドに沿い一貫させる |
| Files | `with` などで確実に閉じる |
| TODO | `TODO(name):` 形式 |
| Import format | 1行1 import。標準 / サードパーティ / ローカルのグループ分け |
| Statements | 原則1行1文 |
| Naming | `snake_case` 関数・変数、`CapWords` クラス、`ALL_CAPS` 定数。`l`/`O`/`I` の1文字名は避ける |
| Main | 副作用のない import。実行入口は `main()` + `if __name__ == '__main__':` |
| Function length | 小さく焦点を絞る。長すぎたら分割を提案 |

## 命名早見

- 関数・メソッド・変数: `lower_with_under`
- クラス・例外: `CapWords`
- 定数: `CAPS_WITH_UNDER`
- 「内部」: 先頭 `_`
- 避ける: `l`, `O`, `I`、既存の組み込み名のシャドウ

## よくある修正パターン

```python
# Bad: mutable default
def f(items=[]):
    items.append(1)

# Good
def f(items=None):
    if items is None:
        items = []
```

```python
# Bad
if x == None:
    ...

# Good
if x is None:
    ...
```

```python
# Bad: 複雑な内包表記
result = [(x, y) for x in xs for y in ys if cond(x, y)]

# Good: 明示的なループ
result = []
for x in xs:
    for y in ys:
        if cond(x, y):
            result.append((x, y))
```

```python
# Good: エントリポイント
def main():
    ...


if __name__ == '__main__':
    main()
```
