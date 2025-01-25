#시간복잡도를 고려한 코드 -> O(N)₩2
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
gold = 0

# 초기 최대값과 그 인덱스 찾기
max_value = max(cards)
max_index = cards.index(max_value)

while len(cards) > 1:
    # 현재 최대값과 그 인덱스 사용
    i = max_index
    
    # 왼쪽과 오른쪽 값 계산
    left = cards[i - 1] if i > 0 else float('inf')  # 첫 번째 카드 예외 처리
    right = cards[i + 1] if i < len(cards) - 1 else float('inf')  # 마지막 카드 예외 처리

    # 더 작은 값을 골드에 추가하고, 리스트에서 제거
    if left < right:
        gold += cards[i] + left
        cards.pop(i - 1)  # 왼쪽 제거
        max_index -= 1  # 왼쪽을 제거했으니 인덱스 조정
    else:
        gold += cards[i] + right
        cards.pop(i + 1)  # 오른쪽 제거

    # 현재 최대값이 사라졌다면 새로운 최대값 찾기
    if i >= len(cards) or cards[i] != max_value:
        max_value = max(cards)
        max_index = cards.index(max_value)

print(gold)
