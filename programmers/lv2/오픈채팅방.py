def solution(record):
    answer = []
    user_dict = {}

    for i in record:
        event = i.split()
        if event[0] in ["Enter", "Change"]:
            user_dict[event[1]] = event[2]

    for i in record:
        event = i.split()
        if event[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(user_dict[event[1]]))
        elif event[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(user_dict[event[1]]))

    return answer