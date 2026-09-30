from __future__ import annotations

import argparse
import json
from pathlib import Path

from .adapters import PLANNED_ADAPTERS
from .db import MissionStore
from .planner import ExperimentCandidate, Outcome, rank_experiments
from .recovery import RecoveryMetrics, recovery_score


def cmd_init(args: argparse.Namespace) -> int:
    path = Path(args.db)
    with MissionStore(path) as store:
        mission_id = store.create_mission(args.name, args.authorization)
    print(json.dumps({"db": str(path), "mission_id": mission_id}, indent=2))
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    metrics = RecoveryMetrics(
        class_coverage=args.classes,
        method_body_coverage=args.methods,
        package_coverage=args.packages,
        entrypoint_coverage=args.entrypoints,
        semantic_density=args.semantic,
        native_dependency=args.native,
    )
    print(json.dumps({"semantic_recovery_score": recovery_score(metrics)}, indent=2))
    return 0


def cmd_adapters(_: argparse.Namespace) -> int:
    print(json.dumps(PLANNED_ADAPTERS, indent=2, sort_keys=True))
    return 0


def cmd_plan_demo(_: argparse.Namespace) -> int:
    prior = [0.5, 0.3, 0.2]
    candidates = [
        ExperimentCandidate(
            "compare loaded DEX before/after feature",
            1.0,
            [
                Outcome("new_dex", 0.55, [0.8, 0.15, 0.05]),
                Outcome("no_change", 0.45, [0.25, 0.45, 0.30]),
            ],
        ),
        ExperimentCandidate(
            "repeat static string scan",
            0.6,
            [
                Outcome("signal", 0.20, [0.55, 0.30, 0.15]),
                Outcome("no_signal", 0.80, [0.45, 0.32, 0.23]),
            ],
        ),
    ]
    print(json.dumps(rank_experiments(prior, candidates), indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="traceforge")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="create a mission database")
    p_init.add_argument("--db", default="mission.db")
    p_init.add_argument("--name", required=True)
    p_init.add_argument(
        "--authorization",
        required=True,
        help="why you are authorized to analyze this target",
    )
    p_init.set_defaults(func=cmd_init)

    p_score = sub.add_parser("score", help="calculate semantic recovery score")
    for name in ("classes", "methods", "packages", "entrypoints", "semantic", "native"):
        p_score.add_argument(f"--{name}", type=float, required=True)
    p_score.set_defaults(func=cmd_score)

    p_adapters = sub.add_parser("adapters", help="show planned tool adapters")
    p_adapters.set_defaults(func=cmd_adapters)

    p_plan = sub.add_parser("plan-demo", help="show information-gain experiment ranking")
    p_plan.set_defaults(func=cmd_plan_demo)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.func(args))
