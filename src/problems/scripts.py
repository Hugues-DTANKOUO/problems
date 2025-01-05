import subprocess
from pathlib import Path

path = Path(__file__).parent


def run_lint() -> None:
    """Run ruff format, ruff check and mypy."""

    print("Running ruff format")
    subprocess.run(["ruff", "format", path], check=True)

    print("Running ruff check")
    subprocess.run(["ruff", "check", path], check=True)

    print("Running mypy")
    subprocess.run(["mypy", path], check=True)


def run_tests() -> None:
    """Run pytest."""
    print("Running pytest")
    try:
        subprocess.run(["pytest", path, "-v"], check=True)
    except subprocess.CalledProcessError:
        print("Tests failed")
        exit(1)


def run_all_checks() -> None:
    """Run all checks."""
    run_lint()
    run_tests()
