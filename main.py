import numpy as np

ACTIONS = ["LEFT", "UP", "RIGHT", "DOWN"]


def parse(filename):
    with open(filename) as f:
        data = [l.strip() for l in f.readlines()]

    n_states = int(data[0])

    rewards = [float(d) for d in data[1:1 + n_states]]

    actions = {}
    start = 1 + n_states
    end = start + n_states
    for action in ACTIONS:
        transition = [[float(p) for p in l.split(",")] for l in data[start:end]]
        actions[action] = transition

        start = end
        end = start + n_states

    return n_states, rewards, actions


def value_iteration(n_states, rewards, gamma, actions, epsilon):
    u_prime = np.zeros(n_states)

    while True:
        u = u_prime.copy()
        delta = 0

        for state in range(n_states):
            tmp = []
            for action in actions:
                transition = actions[action]

                s = 0
                for state_prime in range(n_states):
                    p = transition[state][state_prime]
                    s += p * u_prime[state_prime]

                tmp.append(s)

            u_prime[state] = rewards[state] + gamma * max(tmp)

            diff = abs(u[state] - u_prime[state])
            if diff > delta:
                delta = diff

        if delta <= epsilon * (1 - gamma) / gamma:
            break

    return u


def problem1():
    n_states, rewards, actions = parse("data/gw1.txt")
    u = value_iteration(n_states, rewards, 1, actions, 0.1)
    print(u[:24].reshape(4, 6))


def problem2():
    n_states, rewards, actions = parse("data/gw2.txt")
    u = value_iteration(n_states, rewards, 1, actions, 0.1)


def main():
    problem1()
    # problem2()


if __name__ == "__main__":
    main()
