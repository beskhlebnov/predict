
def markov(data):
    try:
        P_rr = data['P_rr']
        P_rp = data['P_rp']
        P_pp = data['P_pp']
        P_pr = data['P_pr']

        if data['start'] == 'up':
            P_r = 1.0
            P_p = 0.0
        else:
            P_r = 0.0
            P_p = 1.0

        def calculate_probabilities(P_r, P_p):
            P_r_next = P_r * P_rr + P_p * P_pr
            P_p_next = P_p * P_pp + P_r * P_rp
            return P_r_next, P_p_next

        answer = {"День": [],"Рр": [P_r], "Рп": [P_p]}
        for day in range(1, data['days']+1):
            P_r, P_p = calculate_probabilities(P_r, P_p)
            answer["Рр"].append(round(P_r, 6))
            answer["Рп"].append(round(P_p, 6))
            answer["День"].append(day)
        print(answer)
        return answer
    except Exception as e:
        return "error"