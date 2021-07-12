def check(place):
    # P = 지원자
    # O = 빈 자리
    # X = 파티션

    length = len(place)
    for i in range(length):
        for j in range(length):
            # i+1, i+2
            # j+1, j+2
            # (i+1, j+1) (i+1, j-1)
            if place[i][j] == "P":
                if i+1 < length:
                    if place[i+1][j] == "P":
                        return 0

                if i+2 < length and place[i+2][j] == "P":
                    if place[i+1][j] != "X":
                        return 0

                if j+1 < length:
                    if place[i][j+1] == "P":
                        return 0

                if j+2 < length and place[i][j+2] == "P":
                    if place[i][j+1] != "X":
                        return 0

                if i+1 < length and j+1 < length:
                    if place[i+1][j+1] == "P":
                        if place[i+1][j] != "X" or place[i][j+1] != "X":
                            return 0

                if i+1 < length and 0 <= j-1 < length:
                    if place[i+1][j-1] == "P":
                        if place[i+1][j] != "X" or place[i][j-1] != "X":
                            return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        result = check(place)
        answer.append(result)
    return answer

