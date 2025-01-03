import pandas as pd
def triangular(message):
    try:
        data = message.text.split("\n")
        experts = []
        mins = []
        maxs = []
        modes = []
        P = {0.95: [], 0.90: [], 0.85: []}
        probability = [0.95, 0.90, 0.85]
        for i in range(len(data)):
            lists = list(map(int, data[i].split()))
            experts.append(f"Э{i + 1}")
            mins.append(round(float(lists[0]), 3))
            maxs.append(round(float(lists[1]), 3))
            modes.append(round(float(lists[2]), 3))
        experts.append("Все")
        mins.append(min(mins))
        maxs.append(max(maxs))
        modes.append(sum(modes) / len(modes))
        answer = (f"Если p <= (c - a)/(b - a) \nX = a + √((b - a) * (c - a))"
                  f"\n\nЕсли p > (c - a)/(b - a)\nX = b - √((1-p) * (b - a) * (b - c)\n\n")
        for i in range(len(experts)):
            min_a = mins[i]
            max_b = maxs[i]
            moda_c = modes[i]
            ceta = round((modes[i] - mins[i]) / (maxs[i] - mins[i]), 3)
            answer += f"{experts[i]}: a={mins[i]} b={maxs[i]} c={modes[i]}\n"
            answer += f"\n(c - a)/(b - a) = {ceta}\n"
            for p in probability:
                if p <= ceta:
                    answer += f"{p} <= {ceta}"
                    x = min_a + (p * (max_b - min_a) * (moda_c - min_a)) ** 0.5
                    answer += f"\n => x = {min_a} + √({max_b} - {min_a}) * ({moda_c - min_a}) = {round(x, 3)}\n"
                    P[p].append(round(x, 3))
                else:
                    answer += f"{p} > {ceta}"
                    x = max_b - ((1 - p) * (max_b - min_a) * (max_b - moda_c)) ** 0.5
                    answer += f"\n => x = {min_a} - √(({round(1 - p, 6)}) * ({max_b} - {min_a}) * ({max_b} - {moda_c})) = {round(x, 3)}\n"
                    P[p].append(round(x, 3))
            answer += "\n"

        dt = {"Эксперты": experts, "Мин": mins, "Макс": maxs, "Вероятное": modes,
              "95%": P[0.95], "90%": P[0.90], "85%": P[0.85]}

        df = pd.DataFrame(dt)
    except Exception as e:
        pass