import subprocess
import os

def test_cli_output():
    path = os.path.abspath("sample_data/matches.txt")
    result = subprocess.run(
        ["python", "-m", "league_ranker.main", "--file", path],
        capture_output=True,
        text=True,
        cwd="src"  # Needed because we run inside the module
    )
    assert result.returncode == 0
    assert "1. Tarantulas" in result.stdout


