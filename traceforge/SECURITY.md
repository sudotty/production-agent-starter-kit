# Security and Responsible Use

Traceforge is built for owned or explicitly authorized Android application
security research.

## Scope boundary

Use Traceforge only where you have a legitimate right to inspect the target,
such as:

- your own software,
- an employer/client engagement with explicit authorization,
- a CTF or lab,
- defensive malware analysis,
- lawful interoperability research.

Do not use project components to automate unauthorized access, credential theft,
account takeover, destructive actions, or exploitation of unrelated third-party
systems.

## Capability classes

Traceforge's intended policy model has three classes:

1. **observe** — read-only inspection/acquisition,
2. **mutate** — changes instrumented process/device state,
3. **destructive** — deletion, corruption, or external side effects.

The default profile should remain observation-first.

## External tools

Traceforge will integrate with third-party tools, but should not silently trust
them. Production-ready adapters should record:

- exact tool version,
- upstream source,
- content hash where practical,
- build provenance,
- capability set,
- verification status.

## Reporting vulnerabilities

Do not publish exploit details for an uncoordinated third-party vulnerability
through this repository. Use the affected vendor's security process or a
responsible disclosure channel.

## Secrets

Never commit live credentials, captured session tokens, customer data, private
APK samples, or proprietary decompiled source to the public repository.
