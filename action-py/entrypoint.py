#!/usr/bin/env python3

import os
print('Starting...')

print(os.environ)

repo = os.environ["INPUT_FULL_REPO_NAME"]
print(f'{repo}')

print('Done!')
