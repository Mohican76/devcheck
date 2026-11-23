# devcheck

A small CLI that reports whether a machine is ready for development: OS, free disk, and whether Docker and Git are installed.

![CI](https://github.com/Mohican76/devcheck/actions/workflows/ci.yml/badge.svg)

## Usage

```bash
python3 devcheck.py --os
python3 devcheck.py --disk
python3 devcheck.py --tools
python3 devcheck.py          # prints help
