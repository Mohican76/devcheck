import argparse
import platform
import shutil
import subprocess
from pathlib import Path


def os_info():
    return f"{platform.system()} {platform.release()}"


def disk_free_gb():
    return round(shutil.disk_usage(Path.home()).free / (1024 ** 3), 1)


def tool_version(name):
    if shutil.which(name) is None:
        return f"{name}: not installed"
    try:
        out = subprocess.run(
            [name, "--version"], capture_output=True, text=True, timeout=5
        )
        line = (out.stdout or out.stderr).strip().splitlines()[0]
        return f"{name}: {line}"
    except Exception as exc:
        return f"{name}: error ({exc})"


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="devcheck", description="Check this machine's dev readiness"
    )
    parser.add_argument("--os", action="store_true", help="show OS info")
    parser.add_argument("--disk", action="store_true", help="show free disk space")
    parser.add_argument(
        "--tools", action="store_true", help="check docker and git versions"
    )
    args = parser.parse_args(argv)

    if args.os:
        print(os_info())
    if args.disk:
        print(f"free disk: {disk_free_gb()} GB")
    if args.tools:
        print(tool_version("docker"))
        print(tool_version("git"))
    if not (args.os or args.disk or args.tools):
        parser.print_help()
    return 0


if __name__ == "__main__":

    raise SystemExit(main())
