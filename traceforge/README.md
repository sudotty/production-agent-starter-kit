# Traceforge

> Evidence-driven Android reverse engineering for humans and agents.

Traceforge is an experimental research harness for **authorized Android security analysis**. It is not a one-click unpacker and it does not assume one tool can explain an application.

Instead, Traceforge treats reverse engineering as an iterative scientific process:

**observe → hypothesize → experiment → verify → preserve evidence → reduce uncertainty**

The long-term goal is to give Codex, Claude Code, and other capable coding agents a durable, inspectable workspace for Android RE without turning the chat transcript into the source of truth.

## Why Traceforge?

Modern Android applications can distribute behavior across:

- DEX and dynamically loaded code
- ART runtime structures
- JNI and native libraries
- encrypted or unpacked-at-runtime artifacts
- HTTP/WebSocket APIs
- local storage and IPC
- WebView / JavaScript bridges
- obfuscators, packers, virtual machines, and generated code

Traditional workflows usually produce a pile of terminal output, screenshots, decompiler tabs, Frida scripts, and notes. An LLM can operate those tools, but without durable state it easily repeats work, over-trusts a noisy result, or loses the difference between **a file being dumped** and **the application semantics actually being recovered**.

Traceforge is designed around that gap.

## The core idea

A tool invocation is not a conclusion.

A recovered DEX is an **artifact**. A Frida log line is an **observation**. "The payment module is dynamically loaded" is a **hypothesis** until evidence supports it. A claim becomes durable only when Traceforge can point back to the artifacts, observations, experiments, and verification that justify it.

\`\`\`mermaid
flowchart TD
    A[Codex / LLM Reasoner] --> B[Capability Router]
    B --> C[Skills / Workflows]
    C --> D1[Static adapters]
    C --> D2[Runtime adapters]
    C --> D3[Device adapters]
    D1 --> E[Artifact Normalizer]
    D2 --> E
    D3 --> E
    E --> F[(mission.db)]
    F --> G[Facts]
    F --> H[Hypotheses]
    F --> I[Experiments]
    G --> J[Evidence Graph]
    H --> J
    I --> J
    J --> K[Independent Verification]
    K --> A
\`\`\`

## What makes it different?

### 1. Mission state, not chat history

Traceforge stores durable research state in SQLite. A new agent session can see what was already tested, what failed, what remains uncertain, and which conclusions are actually supported.

The initial schema covers:

\`targets / artifacts / observations / entities / relations / claims / hypotheses / experiments / runs / failures / decisions / tools / capabilities\`

### 2. Semantic recovery, not "dump succeeded"

Traceforge separates acquisition success from semantic recovery.

A DEX can be dumped successfully while still containing empty method bodies, missing business packages, unresolved entrypoints, or native-only logic. The initial Recovery Score models:

- class coverage
- method-body coverage
- package coverage
- entrypoint coverage
- semantic density
- native dependency penalty

### 3. Experiments ranked by information gain

The planner interface ranks candidate experiments by expected entropy reduction per unit cost.

The question is not:

> What can the agent run next?

It is:

> Which reversible experiment is expected to reduce uncertainty the most?

This is the bridge between OODA, Bayesian reasoning, and practical RE automation.

### 4. Multiple observation planes

Traceforge is designed to normalize evidence from multiple tool families rather than crown one "best" tool.

Planned adapters include:

| Plane | Planned integration | Role |
|---|---|---|
| Static | areclaw / JADX / APKiD | baseline structure and code |
| Runtime DEX | clsdumper | ART / DEX observation |
| Runtime native | soSaver | in-memory ELF/.so acquisition |
| Instrumentation | phantom-frida / Frida MCP | dynamic observation |
| Device | ADB MCP | UI, logcat, package and device state |
| Native RE | Ghidra MCP | functions, xrefs, decompilation, callgraph |
| Baseline AppSec | MobSF MCP | standardized static/dynamic baseline |

These projects are independent upstream projects. Traceforge does not vendor or claim ownership of them.

### 5. Verification is a first-class stage

Agent output is not automatically promoted to fact.

Traceforge aims to make it normal to ask:

- Can a second observation path reproduce the claim?
- Does the decompiler parse the artifact?
- Do runtime-loaded classes match the recovered classes?
- Did the observation happen before or after the user action?
- What evidence would falsify the hypothesis?

## Quickstart

Traceforge currently ships a small stdlib-only Python core.

\`\`\`bash
cd traceforge
python -m venv .venv
source .venv/bin/activate
pip install -e .

traceforge init \
  --name "authorized-apk-lab" \
  --authorization "Application owned by my organization; internal security test."

traceforge adapters

traceforge score \
  --classes 0.90 \
  --methods 0.65 \
  --packages 0.85 \
  --entrypoints 0.80 \
  --semantic 0.70 \
  --native 0.20

traceforge plan-demo
\`\`\`

The current release is a **foundation**, not a finished automated reverse-engineering product. Real tool adapters are deliberately staged behind explicit interfaces so each one can be tested, permissioned, and independently verified.

## Research workflow

\`\`\`text
Acquire + hash target
        │
        ▼
Static reconnaissance
        │
        ▼
Build hypotheses
        │
        ▼
Choose lowest-risk / highest-information experiment
        │
        ├── static observation
        ├── runtime DEX observation
        ├── runtime SO observation
        ├── UI differential
        ├── network observation
        └── native analysis
        │
        ▼
Normalize artifacts + observations
        │
        ▼
Update mission.db
        │
        ▼
Verify / falsify
        │
        ▼
Choose next experiment
\`\`\`

## Example: packed application

Traceforge does **not** hard-code "packed APK → run one unpacker."

A stronger workflow is:

\`\`\`text
APK
 ├─ identify framework / ABI / protection signals
 ├─ measure static semantic quality
 └─ form hypotheses
        │
        ▼
runtime timeline
        │
        ├─ loaded DEX delta
        ├─ loaded SO delta
        ├─ class delta
        ├─ network delta
        └─ crypto / storage observations
        │
        ▼
semantic recovery score
        │
        ├─ sufficient → continue analysis
        └─ insufficient
             ├─ missing managed code? inspect ART / DEX plane
             ├─ native-heavy? move to native plane
             └─ VM-like behavior? prioritize semantic reconstruction
\`\`\`

The goal is to understand **where information must become observable for the application to function**, rather than blindly attacking the most heavily protected layer.

## 5W2H

| Question | Traceforge answer |
|---|---|
| What? | An evidence-driven Android RE research harness |
| Why? | Tool output alone is not durable knowledge; agents need state, verification and adaptive planning |
| Who? | Mobile AppSec, internal red teams, reverse engineers, interoperability and malware-analysis labs with authorization |
| When? | Static analysis is insufficient, runtime behavior matters, or investigations span multiple sessions/tools |
| Where? | Analyst workstation + owned/authorized Android test device or emulator |
| How? | Skills + typed adapters + mission DB + evidence graph + OODA/Bayesian planning |
| How much? | Core is OSS-oriented; practical cost is devices, compute/model usage and tool maintenance |

## Authorization boundary

Traceforge is intended for:

- applications you own
- applications you are explicitly authorized to test
- CTFs, labs, training targets, and research samples
- defensive malware analysis and interoperability research where lawful

Traceforge is not intended to automate unauthorized access, credential theft, account takeover, or exploitation of third-party systems.

The project design intentionally separates **observation**, **mutation**, and **destructive** capabilities so future adapters can enforce policy and require explicit authorization.

See [SECURITY.md](SECURITY.md).

## Project structure

\`\`\`text
traceforge/
├── AGENTS.md
├── ROADMAP.md
├── SECURITY.md
├── CONTRIBUTING.md
├── docs/
├── skills/
├── examples/
├── src/traceforge/
│   ├── adapters/
│   ├── db.py
│   ├── models.py
│   ├── planner.py
│   ├── recovery.py
│   └── schema.sql
└── tests/
\`\`\`

## Roadmap at a glance

**0.1 — Foundation**
- mission.db and evidence model
- Recovery Score
- experiment ranking
- adapter protocol
- Skill skeletons

**0.2 — Observation plane**
- clsdumper and soSaver adapters
- Frida/ADB structured event normalization
- temporal snapshots and differential engine

**0.3 — Native + graph**
- Ghidra MCP adapter
- cross-plane entity resolution
- Java ↔ JNI ↔ native ↔ API graph

**0.4 — Agent loop**
- capability retrieval
- hypothesis lifecycle
- information-gain planner
- independent verifier role
- resumable missions

**1.0 — Reproducible research harness**
- benchmark corpus
- compatibility matrix
- signed/provenanced tool lock
- policy profiles
- stable adapter API

Full roadmap: [ROADMAP.md](ROADMAP.md).

## Design influences

Traceforge is informed by several public projects and patterns, including areclaw/areclaw-plugin, clsdumper, soSaver, phantom-frida, Marrow, SkillSeek, durable-agent mission-state patterns, Frida MCP, ADB MCP, Ghidra MCP and MobSF MCP.

The design principle taken from this ecosystem is simple:

> Better models help, but a good harness determines whether intelligence turns into reproducible research.

## Status

**Alpha / architecture-first.**

The repository intentionally starts with a small, inspectable core. The next milestone is not "support every protector." It is to prove that one authorized target can be investigated more reproducibly with evidence state + differential experiments than with an unstructured terminal/chat workflow.

If that benchmark fails, the architecture should change before more adapters are added.

## Contributing

Contributions are welcome around:

- artifact normalization
- evidence schemas
- safe adapter interfaces
- Android runtime compatibility research
- benchmark design
- deterministic verification
- documentation and reproducibility

Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

MIT.
