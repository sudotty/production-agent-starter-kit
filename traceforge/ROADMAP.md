# Traceforge Roadmap

The roadmap is ordered by research leverage, not feature count.

## v0.1 — Foundation

Goal: make a reverse-engineering mission resumable and inspectable.

- [x] SQLite mission schema
- [x] Fact / hypothesis / experiment primitives
- [x] semantic Recovery Score
- [x] expected information-gain planner primitive
- [x] tool adapter protocol
- [x] integration catalog
- [x] initial Skill map
- [ ] artifact content-addressed store
- [ ] claim/evidence CRUD API
- [ ] mission export/import
- [ ] JSON schema for adapter events

Exit criterion: a mission can be stopped, resumed, and audited without reading
the original chat transcript.

## v0.2 — Observation Plane

Goal: normalize runtime observations from owned/authorized Android targets.

- [ ] clsdumper adapter
- [ ] soSaver adapter
- [ ] Frida MCP adapter
- [ ] ADB MCP adapter
- [ ] APKiD/JADX baseline adapter
- [ ] timestamped runtime snapshots
- [ ] DEX/class/SO/network/storage differential engine
- [ ] artifact hashing + provenance
- [ ] policy gate for runtime mutation

Exit criterion: the same experiment produces comparable structured observations
across repeated runs.

## v0.3 — Semantic Recovery

Goal: measure whether recovered artifacts contain useful behavior.

- [ ] class/package coverage estimator
- [ ] method-body completeness estimator
- [ ] entrypoint resolver
- [ ] runtime-loaded vs recovered class comparison
- [ ] native dependency estimator
- [ ] Recovery Score calibration
- [ ] benchmark: packed but authorized test apps
- [ ] distinguish acquisition success from semantic recovery success

Exit criterion: benchmark results correlate with analyst-rated usefulness better
than "DEX file exists."

## v0.4 — Native + Cross-Plane Graph

Goal: connect managed and native behavior.

- [ ] Ghidra MCP adapter
- [ ] JNI boundary resolver
- [ ] DEX class ↔ JNI method ↔ native function links
- [ ] API endpoint entities
- [ ] UI/action entities
- [ ] cross-plane Evidence Graph
- [ ] native artifact validation

Exit criterion: Traceforge can answer "which UI action reaches which native
function/API endpoint, and what evidence supports that path?"

## v0.5 — Adaptive Agent Loop

Goal: choose experiments rather than execute checklists.

- [ ] capability retrieval / Skill router
- [ ] hypothesis priors and posterior updates
- [ ] expected information-gain planner
- [ ] experiment cost/risk model
- [ ] verifier / skeptic role
- [ ] stop conditions
- [ ] failure-memory and retry policy
- [ ] long-running mission resume

Exit criterion: on a benchmark suite, the planner reaches equivalent or better
evidence coverage with fewer low-value experiments than a fixed workflow.

## v0.6 — Reproducibility & Supply Chain

- [ ] tool-lock manifest
- [ ] SHA-256 verification
- [ ] version/provenance recording
- [ ] SBOM
- [ ] reproducible container/dev environment
- [ ] signed release artifacts
- [ ] adapter compatibility matrix
- [ ] external verifier fixtures

## v1.0 — Research Harness

- stable adapter API
- documented policy profiles
- public benchmark methodology
- reproducible mission bundles
- portable evidence graph
- CI-tested core
- compatibility-tested reference integrations
- clear separation of observe / mutate capabilities

## Non-goals

Traceforge will not optimize for:

- "one-click bypass everything" claims,
- stealth claims without runtime verification,
- quantity of integrations over evidence quality,
- autonomous destructive behavior,
- replacing human authorization and scope judgment.
