#formatador de nome : recebe o primeiro e ultimo de uma pessoa e retorna os nomes com apenas as inciais em caixa alta






def format_name(f_name,l_name):
    fname_split=string_list(f_name)
    lname_split=string_list(l_name)

    fname_split[0]=fname_split[0].upper()
    lname_split[0]=lname_split[0].upper()

    f_name=''.join(fname_split)
    l_name=''.join(lname_split)
    print(f'{f_name} {l_name}')

name=input()
last_name=input()

format_name(name,last_name)

