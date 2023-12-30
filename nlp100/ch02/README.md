# ch02

## Pandas
![Alt text](image.png)

## Getting Started
install testing library
```
pip install pytest
```

windows only
```
wsl
```

run test (`ch02`ではなく、`NLP100_2023`で実行すること)
```
pytest ./nlp100/ch02 -v --capture=no --log-cli-level=DEBUG
```

エラーがなければok

## Tips
* windowsならwsl推奨
* pandas使うよ
* シェルの出力はsubprocess