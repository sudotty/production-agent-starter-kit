# Contributing

Traceforge values evidence quality over feature count.

## Good contributions

- structured adapter interfaces
- deterministic artifact parsers
- evidence normalization
- benchmark fixtures that are safe to redistribute
- compatibility tests
- Recovery Score calibration
- information-gain planning
- provenance and supply-chain controls
- clear documentation

## Before opening a change

1. Keep the use case within owned/authorized security research.
2. Explain what uncertainty the feature reduces.
3. Identify the artifact/observation schema it emits.
4. Define how success is independently verified.
5. Add or update tests where feasible.

## Adapter design

Adapters should return structured observations/artifacts rather than human prose.

Avoid:
\`\`\`text
"Looks like 3 DEX files were dumped successfully."
\`\`\`

Prefer:
\`\`\`json
{
  "event": "dex.observed",
  "sha256": "...",
  "size": 12345,
  "strategy": "art_walk",
  "run_id": 42
}
\`\`\`

## Pull requests

Keep changes narrow. State assumptions and known limitations. If compatibility
is only tested against one Android/Frida/tool version, say so explicitly.
