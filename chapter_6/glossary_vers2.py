# printing glossary terms and definitions by using a loop
# the glossary should be expandable

python_glossary = {
    'tuple' : 'a fixed list that cannot be changed',
    'dictionary' : 'a collection of key-value pairs',
    'boolean' : 'a statement that is either true or false',
    'syntax' : 'correct way of stating something',
    'python' : 'a programming language',
    'nmap' : 'a port scanning tool',
    'metasploit' : 'a collection of modules to assist in pen testing',
    'burp suite' : 'a web proxy for testing web apps',
    'dirbuster' : 'a tool for brute forcing directories',
    'hashcat' : 'a tool for hashing and cracking passwords',
}

for key, value in python_glossary.items():
    print(f"\nTerm: {key.title()}")
    print(f"\t{value}")
