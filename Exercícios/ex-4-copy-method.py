import copy

L1 = [10, 20, 30, [40, 50], 60]
print(f"L1: {L1}")

L2 = L1
print(f"L2: {L2}")

L3 = copy.copy(L1)
print(f"L3: {L3}")

L4 = L1[:]
print(f"L4: {L4}")

L5 = L1.copy()
print(f"L5: {L5}")

L6 = list(L1)
print(f"L6: {L6}")

L7 = copy.deepcopy(L1)
print(f"L7: {L7}")
