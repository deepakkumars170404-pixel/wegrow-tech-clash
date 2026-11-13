import json

with open('D:/WEGROW/14.Game/public/questions.json', encoding='utf-8') as f:
    data = json.load(f)

for i, r in enumerate(data):
    ans_seq = [q.get('ans') for q in r['questions'] if 'ans' in q]
    letters = ['ABCD'[a] if isinstance(a, int) and 0 <= a <= 3 else str(a) for a in ans_seq]
    print(f"R{i+1}: {r['name'][:32]} -> {letters}")
