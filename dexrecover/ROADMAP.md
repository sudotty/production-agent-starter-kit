# DexRecover Roadmap

DexRecover stays intentionally narrow:

**runtime DEX acquisition → validation → comparison → recovery quality**

## v0.1 — DEX Evidence

- [x] scan DEX/CDEX capture directories
- [x] SHA-256 artifact identity
- [x] duplicate detection
- [x] basic header validation
- [x] before/after capture comparison
- [x] recovery score primitive
- [x] next-step recommendation
- [ ] manifest JSON schema
- [ ] richer DEX header checks

Exit criterion: two capture directories can be compared reproducibly without manual file bookkeeping.

## v0.2 — clsdumper Integration

- [ ] read clsdumper metadata.json
- [ ] retain originating dump strategy
- [ ] merge duplicate artifacts from multiple strategies
- [ ] import capture timestamps
- [ ] clsdumper healthcheck
- [ ] optional clsdumper runner
- [ ] stable normalized capture manifest

Exit criterion: a clsdumper run can feed DexRecover without manual renaming or copying.

## v0.3 — Semantic Recovery Validation

- [ ] method-body presence estimator
- [ ] class/method count
- [ ] business-package coverage
- [ ] runtime-loaded class inventory
- [ ] recovered/runtime class coverage
- [ ] optional JADX validation
- [ ] optional androguard validation
- [ ] benchmark against unprotected ground-truth builds

Exit criterion: the recovery score correlates with whether an analyst can actually read meaningful business logic.

## v0.4 — Guided Runtime Recovery

- [ ] capture labels tied to controlled application events
- [ ] before/after runtime capture workflow
- [ ] narrow strategy recommendation
- [ ] one-command recovery session
- [ ] machine-readable final report

Exit criterion: an authorized protected APK can be analyzed as a repeatable sequence of DEX-recovery experiments.

## v1.0 — Narrow and Dependable

- compatibility matrix by Android / ART / runtime dumper version
- benchmark corpus using redistributable/open test applications
- pinned integration versions
- deterministic reports
- documented failure modes
- stable CLI

## Explicitly out of scope

- full native reverse engineering
- generic mobile vulnerability scanning
- API exploitation
- credential workflows
- broad mobile-device automation
- generic multi-agent orchestration
