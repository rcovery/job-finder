from sys import argv
from argparse import ArgumentParser
from integrations.manager import Manager

def pretty_terminal_output(data):
    for job in data:
        print(f"""\n{'_' * 10}{job['title']}{'_' * 10}\n
        Location: {job['location']}
        Company: {job['company']}
        Summary: {job['summary']}
        Link: {job['link']}
{"_" * (20 + len(job["title"]))}\n""")

parser = ArgumentParser()

parser.add_argument('--region', help='Country that you wanna look for jobs. Ex: "pt", "*", "uk,ca,pt"', required=True)
parser.add_argument('--search', help='Search term. Ex: "Au Pair"')
parser.add_argument('--location', help='Location of jobs. Ex: "Silicon Valley"')

arguments = parser.parse_args()

jora = Manager(integration = 'jora')
response = jora.get(region=arguments.region.split(','), search=arguments.search or None, location=arguments.location or None)

pretty_terminal_output(response)
