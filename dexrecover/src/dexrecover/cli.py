from __future__ import annotations

import argparse
import json

from .capture import load_manifest, save_manifest, scan_capture
from .compare import compare_manifest_dicts
from .score import RecoverySignals, recovery_score
from .strategy import RecoveryState, recommend_next_step


def cmd_scan(args: argparse.Namespace) -> int:
    manifest = scan_capture(args.directory, label=args.label)
    if args.output:
        save_manifest(manifest, args.output)
    print(json.dumps(manifest.to_dict(), indent=2, sort_keys=True))
    return 0


def cmd_diff(args: argparse.Namespace) -> int:
    before = load_manifest(args.before)
    after = load_manifest(args.after)
    delta = compare_manifest_dicts(before, after)
    print(json.dumps(delta.to_dict(), indent=2, sort_keys=True))
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    signals = RecoverySignals(
        valid_dex_ratio=args.valid,
        unique_dex_ratio=args.unique,
        method_body_ratio=args.methods,
        business_package_ratio=args.packages,
        runtime_class_coverage=args.runtime_classes,
    )
    print(json.dumps({"recovery_score": recovery_score(signals)}, indent=2))
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    state = RecoveryState(
        found_dex=args.found,
        structurally_valid=args.valid,
        method_body_ratio=args.methods,
        runtime_class_coverage=args.runtime_classes,
        native_heavy=args.native_heavy,
    )
    print(json.dumps({"next_step": recommend_next_step(state)}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dexrecover",
        description="Validate and compare runtime DEX captures from authorized Android research.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_scan = sub.add_parser("scan", help="catalog and validate dumped DEX/CDEX files")
    p_scan.add_argument("directory")
    p_scan.add_argument("--label")
    p_scan.add_argument("--output")
    p_scan.set_defaults(func=cmd_scan)

    p_diff = sub.add_parser("diff", help="compare two runtime capture manifests")
    p_diff.add_argument("before")
    p_diff.add_argument("after")
    p_diff.set_defaults(func=cmd_diff)

    p_score = sub.add_parser("score", help="calculate semantic recovery quality")
    p_score.add_argument("--valid", type=float, required=True)
    p_score.add_argument("--unique", type=float, required=True)
    p_score.add_argument("--methods", type=float, required=True)
    p_score.add_argument("--packages", type=float, required=True)
    p_score.add_argument("--runtime-classes", type=float, required=True)
    p_score.set_defaults(func=cmd_score)

    p_plan = sub.add_parser("plan", help="recommend the next narrow recovery step")
    p_plan.add_argument("--found", action="store_true")
    p_plan.add_argument("--valid", action="store_true")
    p_plan.add_argument("--methods", type=float)
    p_plan.add_argument("--runtime-classes", type=float)
    p_plan.add_argument("--native-heavy", action="store_true")
    p_plan.set_defaults(func=cmd_plan)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.func(args))
