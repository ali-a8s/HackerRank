if __name__ == '__main__':
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
    combined = dict(sorted(zip(name_list,score_list), key=lambda x: x[0]))
    sorted_score_list = sorted(set(score_list))
    runner_up = sorted_score_list[1]
    for k, v in combined.items():
        if v == runner_up:
            print(k)