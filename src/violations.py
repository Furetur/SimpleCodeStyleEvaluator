from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Mapping


@dataclass
class Violation:
    filepath: str
    line: int
    col: int
    code: str
    message: str
    source: str


def format_violation(violation: Violation):
    return f"{violation.filepath}:{violation.line}:{violation.col}: {violation.code} {violation.message}\n{violation.source}"


GroupedViolations = Mapping[str, List[Violation]]


def group_violations_by_codes(violations: List[Violation]) -> GroupedViolations:
    groups: GroupedViolations = defaultdict(list)
    for violation in violations:
        groups[violation.code].append(violation)
    return groups
