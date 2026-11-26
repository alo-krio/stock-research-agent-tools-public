# Verification records

[results.json](results.json) contains 223 historical, resource-level records. Join a record's `id` to [the registry](../registry/resources.json). A resource may appear in both checks. An absent record means there is no published check for that resource.

| Date | Suite | Published coverage |
|---|---|---|
| 2026-11-25 | Smoke checks | 70 passed. Each row records offline or live mode and the package version when available. |
| 2026-11-24 | Resource audit | 50 offline passes, 27 live passes, 3 cached replay passes, 21 import or component checks, 45 source-document reviews and 7 requiring follow-up. |

In the smoke suite, `pass` means the particular smoke check succeeded. Some checks cover import or construction only. In the resource audit, `offline_pass` denotes a local fixture, `live_pass` a bounded upstream check, and `cached_pass` a replay of saved evidence. `import_only` and `source_only` indicate narrower evidence. `needs_followup` indicates unresolved setup, access or validation.

These are historical outcomes. The release check validated the directory and search interface without rerunning upstream packages or services. To independently evaluate a candidate, follow the relevant [playbook](../playbooks/README.md) using your own data access and environment.
