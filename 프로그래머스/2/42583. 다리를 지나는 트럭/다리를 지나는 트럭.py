def solution(bridge_length, weight, truck_weights):
    answer = 0
    mid_weight = 0  # 현재 다리 위 트럭의 총 무게
    bridge = [0] * bridge_length  # 다리 위 트럭 상태를 저장하는 리스트

    while bridge:
        answer += 1

        # 다리에서 트럭(또는 0) 제거
        exited_truck = bridge.pop(0)
        mid_weight -= exited_truck

        # 대기 중인 트럭이 있는 경우
        if truck_weights:
            # 새 트럭이 다리 위로 올라갈 수 있는지 확인
            if mid_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)
                bridge.append(new_truck)
                mid_weight += new_truck
            else:
                bridge.append(0)  # 트럭이 올라갈 수 없으면 빈 공간 추가

    return answer
