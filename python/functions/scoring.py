def approve(
    gender: str, 
    age: int, 
    score: int
) -> bool:
    if age < 21:
        return False
    if gender == 'M':
        score += 100 if 21 <= age <= 39 else 50
    elif gender == 'F':
        score += 50 if 21 <= age <= 39 else 20
    return True if score > 500 else False

my_gender = input()
my_age = int(input())
my_score = int(input())
print(
    approve(
        gender=my_gender, 
        age=my_age,
        score=my_score
    )
)
