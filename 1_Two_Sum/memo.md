## step1

最初に思いついた方法は、ブルートフォース的に考えて、二重ループを考えた。計算量がO(n^2)になるので適切ではないと思う。
実際に、standalone/step1.pyで要素をランダムにして、実行時間を計測したところ、
N =  100 | 実行時間: 0.1356 ms
N =  500 | 実行時間: 3.2582 ms
N = 1000 | 実行時間: 12.2532 ms
N = 2000 | 実行時間: 41.6920 ms
であった。

## step2

他の方のコードを見てみると、どうやらpythonには、Dictionariesというデータ型があるらしい。
{ key: value }というデータ構造らしい。return indices なので、key: element, value: index が良い?
以下のように書くと、keyを調べてくれるらしい

```python
diff_to_index = {}
...
if complete in diff_to_index:
```
実行計測
N =  100 | 実行時間: 0.0125 ms
N =  500 | 実行時間: 0.0404 ms
N = 1000 | 実行時間: 0.0895 ms
N = 2000 | 実行時間: 0.1590 ms

