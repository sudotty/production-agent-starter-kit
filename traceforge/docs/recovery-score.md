# Recovery Score

Traceforge distinguishes **artifact acquisition** from **semantic recovery**.

A tool can successfully emit a DEX file while the recovered material remains
poor for analysis.

## Initial metric

The v0.1 score uses:

- class coverage: 18%
- method body coverage: 25%
- package coverage: 16%
- entrypoint coverage: 16%
- semantic density: 15%
- native dependency: 10% penalty

The positive metrics are normalized before applying the native-dependency
penalty.

This formula is intentionally provisional.

## Why method bodies have the largest weight

For many protected applications, class/method metadata can survive while code
items are removed, restored lazily, or implemented behind JNI. Counting class
names alone therefore overstates recovery quality.

## Calibration roadmap

A benchmark should collect:

1. ground-truth unprotected build,
2. protected build,
3. recovered artifacts,
4. analyst usefulness rating,
5. runtime-loaded class inventory,
6. entrypoint/call-path coverage.

Weights should be updated from benchmark evidence rather than intuition.
