import subprocess
from parser import Parser
from violations import group_violations_by_codes, format_violation, Violation, GroupedViolations


def run_linter() -> str:
    return subprocess.run(['flake8', 'resources'], capture_output=True, text=True).stdout


def run_and_group_violations() -> GroupedViolations:
    output = run_linter()
    violations = Parser(output).parse()
    return group_violations_by_codes(violations)


def print_grouped_violations(grouped: GroupedViolations):
    for code, violations in grouped.items():
        print(f"\nThere were {len(violations)} violations of type {code}\n")
        for index, violation in enumerate(violations):
            pretty_violation = format_violation(violation)
            print(f"{index + 1}) {pretty_violation}")


if __name__ == "__main__":
    groups = run_and_group_violations()
    print_grouped_violations(groups)
