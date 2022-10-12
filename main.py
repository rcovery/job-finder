from integrations.manager import Manager

def pretty_terminal_output(data):
    for job in data:
        print(f"""\n{'_' * 10}{job['title']}{'_' * 10}\n
        Location: {job['location']}
        Company: {job['company']}
        Summary: {job['summary']}
        Link: {job['link']}
{"_" * (20 + len(job["title"]))}\n""")


jora = Manager(integration = 'jora')
response = jora.get(region='uk', search='Au Pair')

pretty_terminal_output(response)
