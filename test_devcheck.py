import devcheck


def test_os_info_returns_string():
    assert isinstance(devcheck.os_info(), str)
    assert devcheck.os_info()


def test_disk_free_gb_positive():
    assert devcheck.disk_free_gb() > 0


def test_tool_version_missing(monkeypatch):
    monkeypatch.setattr(devcheck.shutil, "which", lambda name: None)
    assert devcheck.tool_version("nope") == "nope: not installed"


def test_main_os(capsys):
    rc = devcheck.main(["--os"])
    out = capsys.readouterr().out
    assert rc == 0
    assert out.strip() == devcheck.os_info()


def test_main_disk(capsys):
    rc = devcheck.main(["--disk"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "free disk:" in out


def test_main_no_args_prints_help(capsys):
    rc = devcheck.main([])
    out = capsys.readouterr().out
    assert rc == 0
    assert "usage: devcheck" in out
