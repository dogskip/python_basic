import random

random_int = random.randint(1, 100)
print(random_int)
print(random.randint(1, 100))

print(random.random())

print(random.randrange(1, 100, 2))

print(random.choice([1, 2, 3, 4, 5]))

print(random.sample([1, 2, 3, 4, 5], 3))

items = ["A", "B", "C"]
weights = [0.7, 0.2, 0.1]
result = random.choices(items, weights, k=10)
print(result)
cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
print(f"섞인 카드: {cards}") 
playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
random.shuffle(playlist)
print(f"새 재생 순서: {playlist}")