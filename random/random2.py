import random

def monte_carlo_pi(num_samples):
    inside = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return (inside / num_samples) * 4

pi_estimate = monte_carlo_pi(10_000_000)
print(f"PI 추정값: {pi_estimate} (오차: {abs(pi_estimate - 3.1415926535):.5f})")
