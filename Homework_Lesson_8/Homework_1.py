import re

def email_parse(email):
    result_pars_dict = {}
    usernames = re.findall("^[aA-zZ,0-9]+", email)
    mail = re.findall("@[aA-zZ,0-9].+$", email)
    if re.search("^[aA-zZ,0-9]+[@]+[aA-zZ,0-9]+[.]+[aA-zZ,0-9]+$", email):
        for username in usernames:
            result_pars_dict['name'] = username
        for i in mail:
            i = str(i).split('@')
        for domains in i:
            if len(domains) > 1:
                result_pars_dict['domain'] = domains
        print(result_pars_dict)
    else:
        raise ValueError('Неправильно введен адрес')



email_parse('some45one@geek45brainsruyy.y45')







