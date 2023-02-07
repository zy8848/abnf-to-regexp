variant = f'(({alphanum}){{5,8}}|[0-9]({alphanum}){{3}})'
singleton = '[0-9A-WY-Za-wy-z]'
script = '[a-zA-Z]{4}'
regular = (
    '(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|'
    'zh-min|zh-min-nan|zh-xiang)'
)
region = '([a-zA-Z]{2}|[0-9]{3})'
privateuse = f'[xX](-({alphanum}){{1,8}})+'
language_tag = f'({langtag}|{privateuse}|{grandfathered})'
language = f'([a-zA-Z]{{2,3}}(-{extlang})?|[a-zA-Z]{{4}}|[a-zA-Z]{{5,8}})'
langtag = (
    f'{language}(-{script})?(-{region})?(-{variant})*(-{extension})*(-'
    f'{privateuse})?'
)
irregular = (
    '(en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|'
    'i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|'
    'i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)'
)
grandfathered = f'({irregular}|{regular})'
extlang = '[a-zA-Z]{3}(-[a-zA-Z]{3}){2}'
extension = f'{singleton}(-({alphanum}){{2,8}})+'
alphanum = '[a-zA-Z0-9]'
