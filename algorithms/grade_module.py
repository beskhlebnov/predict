import pandas as pd
def grade(data):
    df = pd.DataFrame(data)

    df['Сумма (3)'] = df['Значение'].rolling(window=3).sum().round(1)
    df['Cредняя (3)'] = df['Значение'].rolling(window=3).mean().round(1)
    df['Сумма (5)'] = df['Значение'].rolling(window=5).sum().round(1)
    df['Cредняя (5)'] = df['Значение'].rolling(window=5).mean().round(1)

    return df


