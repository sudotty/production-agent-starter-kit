from __future__ import annotations

PLANNED_ADAPTERS = {
    "areclaw": {
        "stage": "planned",
        "capabilities": ["apk-recon", "static-analysis", "workflow"],
    },
    "clsdumper": {
        "stage": "planned",
        "capabilities": ["runtime-dex", "art-observation"],
    },
    "sosaver": {
        "stage": "planned",
        "capabilities": ["runtime-so", "native-artifact"],
    },
    "phantom-frida": {
        "stage": "planned",
        "capabilities": ["instrumentation-runtime"],
    },
    "frida-mcp": {
        "stage": "planned",
        "capabilities": ["runtime-hook", "memory-observation", "java-observation"],
    },
    "adb-mcp": {
        "stage": "planned",
        "capabilities": ["device-control", "ui-observation", "logcat"],
    },
    "ghidra-mcp": {
        "stage": "planned",
        "capabilities": ["native-decompile", "xref", "callgraph"],
    },
    "mobsf-mcp": {
        "stage": "planned",
        "capabilities": ["baseline-sast", "baseline-dast", "report"],
    },
}
