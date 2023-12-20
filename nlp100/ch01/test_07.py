def weather_forecast(x, y, z):
    return f'{x}時の{y}は{z}'

def test_テンプレートによる文生成():
    x = 12
    y = "気温"
    z = 22.4

    result = weather_forecast(x, y, z)

    assert result == "12時の気温は22.4"
