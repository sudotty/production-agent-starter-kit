# DexRecover

> Runtime DEX recovery and validation for protected Android APKs.

This branch is the clean bootstrap of **DexRecover**.

Project source and full documentation:

**[Open DexRecover →](dexrecover/README.md)**

DexRecover intentionally focuses on one problem:

> Given DEX files captured from a running protected Android app, determine what was recovered, what changed between captures, and whether the recovered code is actually useful.

Core flow: **capture → validate → deduplicate → diff → score**.

See [`dexrecover/`](dexrecover/) for the package, tests, 3 focused Agent Skills and vertical roadmap.
