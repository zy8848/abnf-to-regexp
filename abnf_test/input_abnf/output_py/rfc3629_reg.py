utf8_tail = '[\\x80-\\xbf]'
utf8_octets = f'({utf8_char})*'
utf8_char = f'({utf8_1}|{utf8_2}|{utf8_3}|{utf8_4})'
utf8_4 = (
    f'(\\xf0[\\x90-\\xbf]({utf8_tail}){{2}}|[\\xf1-\\xf3]({utf8_tail}){{3}}|'
    f'\\xf4[\\x80-\\x8f]({utf8_tail}){{2}})'
)
utf8_3 = (
    f'(\\xe0[\\xa0-\\xbf]{utf8_tail}|[\\xe1-\\xec]({utf8_tail}){{2}}|\\xed'
    f'[\\x80-\\x9f]{utf8_tail}|[\\xee-\\xef]({utf8_tail}){{2}})'
)
utf8_2 = f'[\\xc2-\\xdf]{utf8_tail}'
utf8_1 = '[\\x00-\\x7f]'
