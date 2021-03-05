from parse import parse
from typing import List

from violations import Violation

blank_characters = {'\n', '\r', '\r\n', ' ', '\t'}


def is_blank(line):
    return set(line).issubset(blank_characters)


class Parser:
    def __init__(self, linter_output):
        self.lines = [line for line in linter_output.split('\n') if not is_blank(line)]

    def parse(self) -> List[Violation]:
        raw_violations = [self.lines[i: i + 3] for i in range(0, len(self.lines), 3)]
        return [self.parse_violation(raw_violation) for raw_violation in raw_violations]

    def parse_violation(self, raw_violation):
        violation_declaration, *source_lines = raw_violation
        source_code = "\n".join(source_lines)
        parsed = parse("{filepath}:{line:d}:{col:d}: {code:w} {msg}", violation_declaration).named
        return Violation(
            parsed['filepath'],
            parsed['line'],
            parsed['col'],
            parsed['code'],
            parsed['msg'],
            source_code
        )
