#!/usr/bin/env python3

import os
print('Starting...')

repo = os.environ['GITHUB_REPOSITORY']
user = os.environ['GITHUB_ACTOR']

print(f'Hello {user} of {repo}!')
