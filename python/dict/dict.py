d: dict = {
    'name': 'Muslim',
    'surname': 'Beibytuly', 
    'age': 22,
    'gender': 'male'
}

languages = {
    'Kazakhstan': 'KZ',
    'Russia': 'RU',
    'Kyrgyzstan': 'RU'
}
current_language = languages.get(
    'Kazakhstan', 'EN'
)
i18n = (
    {
        'greeting': {
            'KZ': 'Salem',
            'EN': 'Hello',
            'RU': 'Privet'
        }
    },
)

current_text = i18n.get(
    'greeting'
    ).get(current_language, 'hello')

d.get('lastname', '')

for k, v in d.items():
    print(k, v)
