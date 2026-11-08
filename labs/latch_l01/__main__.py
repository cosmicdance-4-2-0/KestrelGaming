"""Run public synthetic teaching cases; no learner scoring or qualification."""

import argparse
import json
from dataclasses import asdict

from .visible_cases import run_visible_cases


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print structured public case results")
    args = parser.parse_args(argv)
    outcomes = run_visible_cases()
    passed = sum(case.passed for case in outcomes)
    successful = bool(outcomes) and passed == len(outcomes)
    if args.json:
        print(json.dumps({
            "kind": "public_fixture_run", "case_count": len(outcomes),
            "passed": passed, "failed": len(outcomes) - passed,
            "successful": successful,
            "qualification_assessed": False,
            "cases": [{**asdict(case), "passed": case.passed} for case in outcomes],
        }, indent=2))
    else:
        for case in outcomes:
            print(f"{'PASS' if case.passed else 'FAIL'} {case.name}")
            for check in case.checks:
                if not check.passed:
                    print(f"  {check.label}: {check.detail}")
            if case.error:
                print(f"  error: {case.error}")
        print(f"{passed}/{len(outcomes)} public cases passed.")
        print("Public fixture checks; learner qualification not assessed.")
    return 0 if successful else 1


if __name__ == "__main__":
    raise SystemExit(main())
