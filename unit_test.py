import subprocess

with open('tests_input.sh', 'r', encoding='utf-8') as file:
    for script in file:
        rc = subprocess.call(script, shell=True)
