import json

policy_file = "/opt/_internal/pipx/venvs/auditwheel/lib/python3.10/site-packages/auditwheel/policy/manylinux-policy.json"

with open(policy_file) as fh:
    policies = json.load(fh)

for p in policies:
    p['lib_whitelist'].append('libxcb.so.1')

with open(policy_file, 'w') as fw:
    json.dump(policies, fh)
