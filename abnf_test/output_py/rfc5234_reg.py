rulename = '[a-zA-Z][a-zA-Z0-9\\-]*'
repeat = '([0-9]+|[0-9]*\\*[0-9]*)'
num_val = f'%({bin_val}|{dec_val}|{hex_val})'
hex_val = '[xX][0-9A-Fa-f]+((\\.[0-9A-Fa-f]+)+|-[0-9A-Fa-f]+)?'
defined_as = f'({c_wsp})*(=|=/)({c_wsp})*'
dec_val = '[dD][0-9]+((\\.[0-9]+)+|-[0-9]+)?'
comment = ';[ \t!-~]*\\\r\\\n'
char_val = '"[ -!#-~]*"'
c_wsp = f'([ \t]|{c_nl}[ \t])'
c_nl = f'({comment}|\\\r\\\n)'
bin_val = '[bB][01]+((\\.[01]+)+|-[01]+)?'