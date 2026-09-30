# Planned Integrations

Traceforge favors typed adapters and structured output.

| Integration | Intended role | Initial risk class |
|---|---|---|
| areclaw / areclaw-plugin | domain workflow/reference | observe |
| clsdumper | runtime DEX observations | observe |
| soSaver | runtime native artifact observations | observe |
| phantom-frida | instrumentation runtime | mutate |
| Frida MCP | runtime observation/hooking | observe/mutate |
| ADB MCP | device/UI/logcat | observe/mutate |
| Ghidra MCP | native analysis | observe |
| MobSF MCP | baseline mobile AppSec | observe |

## Adapter maturity labels

- planned
- experimental
- verified-single-environment
- compatibility-tested
- stable

An integration should not be called stable merely because the upstream project
is mature. Traceforge must test its own adapter contract and normalization.
