regions = ["서울", "경기", "인천", "부산"]
populations = ["950만명", "1350만명", "290만명", "340만명"]
famous_spots = ["남산타워", "수원화성", "월미도", "해운대"]
specialties = ["한강", "국제공항", "항구", "광안대교"]

city_data = [
    ["수도권", [regions[0:3], populations[0:3]], "대한민국 중심지"],
    ["영남권", [[regions[3]], [populations[3]]], "제2경제도시"],
    ["전체도시", [regions, populations], "주요 도시권"]
]

for area in city_data:
    print(f"\n{area[0]} 정보:")
    if isinstance(area[1][0], list):
        for city, pop in zip(area[1][0], area[1][1]):
            print(f"- {city}: {pop}")
    print(f"- 특징: {area[2]}")
    print("-" * 30)

local_details = {
    regions[0]: [famous_spots[0], specialties[0]],
    regions[1]: [famous_spots[1], specialties[1]],
    regions[2]: [famous_spots[2], specialties[2]],
    regions[3]: [famous_spots[3], specialties[3]]
}

print("\n각 도시 상세 정보:")
for city, details in local_details.items():
    print(f"\n{city}:")
    print(f"- 명소: {details[0]}")
    print(f"- 특징: {details[1]}")
