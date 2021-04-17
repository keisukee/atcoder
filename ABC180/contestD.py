X, Y, A, B = list(map(int, input().split()))
max_experience_to_gain = 0
current_strength = X

while current_strength < Y:
    # print(current_strength)
    if current_strength * A < current_strength + B:
        current_strength *= A
        max_experience_to_gain += 1
    else:
        if Y - current_strength <= B:
            current_strength += B
            max_experience_to_gain += 1
        else:
            levels = (Y - current_strength) // B
            current_strength += levels * B
            max_experience_to_gain += levels

max_experience_to_gain -= 1
print(max_experience_to_gain)

