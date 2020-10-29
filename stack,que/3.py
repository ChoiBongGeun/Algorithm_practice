def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge= [0] * bridge_length #다리에 아무것도 없고 앞에서부터 하나씩 빠지기 위해 0으로 채운 리스트 생성
    
    while len(bridge) !=0:
        cnt += 1
        bridge.pop(0) #빠질 시간이 된 트럭 빠질수 있게 
        if len(truck_weights) !=0:#올라갈 트럭이 더이상 없으면 리스트에 더해주지 않는다
            if sum(bridge) + truck_weights[0] > weight:# 버틸수 있는 무게보다 높으면 아무것도 안올라갔다는의미에 0을 append
                bridge.append(0)
            else:#아닐경우 트럭에서 하나 빼주고 다리에 올려준다
                truck=truck_weights.pop(0)
                bridge.append(truck)
    answer = cnt
    return answer
