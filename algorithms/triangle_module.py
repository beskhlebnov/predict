import pandas as pd


def triangle(data):
    experts = data["Э"]
    mins = data["min"]
    maxs = data["max"]
    modes = data["moda"]
    result = {0.95: [], 0.90: [], 0.85: []}
    probability = [0.95, 0.90, 0.85]
    abs_trian = []
    for i in range(len(data["Э"])):
        abs_trian.append(round((mins[i]+maxs[i]+modes[i])/3, 1))
    experts.append("Все")
    mins.append(min(abs_trian))
    maxs.append(max(abs_trian))
    modes.append(sum(abs_trian) / len(abs_trian))
    print(mins, maxs, modes)
    for i in range(len(experts)):
        min_a = mins[i]
        max_b = maxs[i]
        moda_c = modes[i]
        ceta = round((modes[i] - mins[i]) / (maxs[i] - mins[i]), 1)
        for p in probability:
            if p <= ceta:
                x = min_a + (p * (max_b - min_a) * (moda_c - min_a)) ** 0.5
                result[p].append(round(x, 1))
            else:
                x = max_b - ((1 - p) * (max_b - min_a) * (max_b - moda_c)) ** 0.5
                result[p].append(round(x, 1))

    dt = {"Эксперт": experts, "Min": mins, "Мax": maxs, "Moda": modes,
          "95%": result[0.95], "90%": result[0.90], "85%": result[0.85]}

    df = pd.DataFrame(dt)
    return df
