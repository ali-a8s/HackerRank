k = int(input())
rooms = list(map(int, input().split()))

unique_room = sum(set(rooms))
total_rooms = sum(rooms)

print((k*unique_room-total_rooms)//(k-1))