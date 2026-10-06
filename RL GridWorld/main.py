grid = [
    ["S", "0", "0", "0"],
    ["0", "X", "0", "0"],
    ["0", "X", "0", "0"],
    ["0", "0", "0", "G"]
]

for row in grid:
    print(row)

robot_position = [0, 0]

print("Robot position:", robot_position)

grid = [
    ["S", "0", "0", "0"],
    ["0", "X", "0", "0"],
    ["0", "X", "0", "0"],
    ["0", "0", "0", "G"]
]

for row in grid:
    print(row)

robot_position = [0, 0]

print("Robot position:", robot_position)

actions = ["up", "down", "left", "right"]

print("Possible actions:", actions)


def move_robot(action):
    row, col = robot_position

    if action == "up" and row > 0:
        row = row - 1

    elif action == "down" and row < 3:
        row = row + 1

    elif action == "left" and col > 0:
        col = col - 1

    elif action == "right" and col < 3:
        col = col + 1

    return [row, col]


new_position = move_robot(actions)

print("New robot position:", new_position)


def get_reward(position):
    if position == [3, 3]:
        return 10
    elif position == [1, 1] or position == [2, 1]:
        return -5
    else:
        return -1


print("Normal:", get_reward([0, 1]))
print("Obstacle:", get_reward([1, 1]))
print("Goal:", get_reward([3, 3]))

q_table = {}

for row in range(4):
    for col in range(4):
        q_table[(row, col)] = [0, 0, 0, 0]


print("Q-table:")
print(q_table)

import random

alpha = 0.1
gamma = 0.9

action = random.choice(actions)

print("Robot chose:", action)

new_position = move_robot(action)

print("Robot moved to:", new_position)

reward = get_reward(new_position)

print("Reward received:", reward)

action_index = actions.index(action)

old_value = q_table[tuple(robot_position)][action_index]

next_max = max(q_table[tuple(new_position)])

new_value = old_value + alpha * (reward + gamma * next_max - old_value)

q_table[tuple(robot_position)][action_index] = new_value

print("Updated Q-value:", q_table[tuple(robot_position)])

robot_position = new_position

print("Current robot position:", robot_position)

for episode in range(500):

    robot_position = [0, 0]

    for step in range(50):

        action = random.choice(actions)

        new_position = move_robot(action)

        reward = get_reward(new_position)

        action_index = actions.index(action)

        old_value = q_table[tuple(robot_position)][action_index]

        next_max = max(q_table[tuple(new_position)])

        new_value = old_value + alpha * (reward + gamma * next_max - old_value)

        q_table[tuple(robot_position)][action_index] = new_value

        robot_position = new_position

        if robot_position == [3, 3]:
            break
    print("\nLearned path:")

robot_position = [0, 0]

for step in range(20):

    print("Position:", robot_position)

    if robot_position == [3, 3]:
        print("🎯 Goal reached!")
        break

    best_action_index = q_table[tuple(robot_position)].index(
        max(q_table[tuple(robot_position)])
    )

    best_action = actions[best_action_index]

    robot_position = move_robot(best_action)