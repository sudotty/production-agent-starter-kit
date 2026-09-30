# DexRecover

> **Recover DEX. Measure what you actually recovered.**

**DexRecover is a small runtime DEX recovery and validation tool for protected Android APKs.**

It sits between **DEX dumping** and **decompilation**:

```text
protected APK
    ↓
runtime DEX capture
(clsdumper / Frida / other authorized workflow)
    ↓
DexRecover
  scan → deduplicate → validate → diff → score
    ↓
JADX / JEB / baksmali
```

DexRecover does one narrow job:

> Given DEX files captured from a running protected Android app, determine what was recovered, what changed between captures, and whether the recovered code is actually useful for analysis.

It is not an Android security platform, not a generic AppSec scanner, and not a "one-click unpack everything" framework.

## Why?

When an Android APK is protected by a packer or runtime loader, static tools may show mostly shell code, loaders, native stubs, or incomplete business logic.

Runtime tools can often recover one or more DEX files, but that creates a second problem:

- Which DEX files are unique?
- Which files are structurally valid?
- Did entering a specific feature load new DEX?
- Are method bodies really present?
- Are the application's business packages recovered?
- Does the recovered class set match what exists at runtime?
- Is "dump succeeded" actually equivalent to "recovery succeeded"?

Usually, it is not.

DexRecover focuses on this exact gap.

## Scope

### DexRecover does

- catalog dumped `.dex` / `.cdex` files
- calculate SHA-256 and deduplicate captures
- validate basic DEX/CDEX structure
- compare **before / after** runtime captures
- measure semantic recovery quality
- recommend the next narrow recovery step
- integrate with runtime DEX dumpers, starting with **clsdumper**

### DexRecover deliberately does not

- perform general mobile AppSec scanning
- map every API endpoint in the application
- reverse arbitrary native libraries
- replace Ghidra, JADX, JEB, Frida, or clsdumper
- become a generic multi-agent security framework
- claim universal support for every commercial protector

If analysis shows that important logic has moved primarily into a native VM or native-only implementation, DexRecover should say so and stop. That boundary is intentional.

## Quick start

Requires Python 3.11+.

```bash
cd dexrecover
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Scan a runtime DEX capture

```bash
dexrecover scan capture-login --output login.json
```

DexRecover records path, SHA-256, size, DEX/CDEX magic, DEX version, declared file size, structural validity and duplicate hashes.

### Compare two runtime moments

```bash
dexrecover scan before-payment --output before.json
dexrecover scan after-payment --output after.json
dexrecover diff before.json after.json
```

If a new DEX appears only after a feature is opened, that is a stronger signal than repeatedly dumping the process without a controlled state change.

### Score recovery quality

```bash
dexrecover score \
  --valid 1.0 \
  --unique 0.9 \
  --methods 0.7 \
  --packages 0.85 \
  --runtime-classes 0.8
```

### Ask for the next recovery step

```bash
dexrecover plan \
  --found \
  --valid \
  --methods 0.35 \
  --runtime-classes 0.60
```

The planner stays narrow: recapture runtime DEX, validate method bodies, compare runtime classes, or hand off native-heavy targets.

## Recovery Score

DexRecover separates **DEX acquisition success** from **semantic recovery success**.

| Signal | Weight |
|---|---:|
| valid DEX ratio | 10% |
| unique DEX ratio | 5% |
| method-body ratio | 35% |
| business-package ratio | 20% |
| runtime-class coverage | 30% |

The weights are provisional and will be calibrated against known ground truth.

## Protected APKs and Jiagu-style packers

DexRecover is relevant to owned or explicitly authorized research involving Android APK packers, dynamically loaded DEX, encrypted DEX restored at runtime, ART-visible code, and Jiagu / 360 Jiagu-style protection scenarios.

This is **not** a claim that DexRecover universally defeats 360 Jiagu or any other commercial protection product. DexRecover focuses on proving what code was actually recovered.

## Why clsdumper first?

The first planned runtime integration is [TheQmaks/clsdumper](https://github.com/TheQmaks/clsdumper).

clsdumper observes multiple points in the DEX lifecycle. DexRecover handles the layer immediately after capture: uniqueness, validity, temporal differences and semantic usefulness.

## Design principle: capture around events

Blind periodic dumping produces noise. DexRecover favors controlled snapshots:

```text
T0 app start
T1 login
T2 open checkout
T3 trigger protected feature
```

For each transition, compare `DEX_after - DEX_before`.

The long-term goal is intentionally small:

> **Find the moment useful DEX becomes observable, recover it, and prove how complete it is.**

## Agent use

DexRecover is agent-friendly but does not require an agent. Codex or another coding agent only needs three small skills:

- `capture-dex`
- `validate-dex`
- `compare-captures`

The agent chooses the next useful DEX-recovery experiment; it does not orchestrate the whole Android security ecosystem.

## Roadmap

- **v0.1:** DEX/CDEX scan, hash, dedup, diff, recovery score
- **v0.2:** direct clsdumper metadata integration and capture timeline
- **v0.3:** method-body, package and runtime-class coverage validation
- **v0.4:** guided `dexrecover recover <package>` workflow
- **v1.0:** documented compatibility and benchmark matrix

See [ROADMAP.md](ROADMAP.md).

## Non-goals

If a feature does not improve runtime DEX acquisition, validation, comparison, or recovery quality, it probably does not belong in DexRecover.

That means no generic vulnerability scanner, network proxy suite, native RE IDE, mobile automation platform, or agent operating system.

**Small surface area is a feature.**

## Responsible use

Use DexRecover only for software you own, are explicitly authorized to test, or may lawfully analyze in a lab/CTF/defensive research context.

See [SECURITY.md](SECURITY.md).

## Search terms

Android DEX recovery · protected APK · APK unpacking · runtime DEX dump · ART · Frida · clsdumper · Android reverse engineering · Jiagu · 360 Jiagu · DEX validation

## Status

**Early alpha.** The next meaningful milestone is clsdumper integration — not more features.

## License

MIT.