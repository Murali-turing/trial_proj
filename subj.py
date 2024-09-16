from harness import Harness
import argparse
import subprocess
import os
import pytest

# ----------------------------------------
# - Test Description
# ----------------------------------------

docker_file    = os.path.join("harness/subj", "subj.yml")

if __name__ == "__main__":

    # Parse Creation
    parser = argparse.ArgumentParser(description="Exemplo de uso do argparse")
    parser.add_argument("-n", "--name", required=True, type=str, help="File that is going to perform the harness subjective evaluation.")

    args = parser.parse_args()

    test = Harness()
    cmd  = test.format_compose(docker_file)
    cmd  = f"{cmd} --env UUT=/code/{args.name} auto"

    result = subprocess.run(cmd, shell=True)
    assert result.returncode == False, "Subjective execution failed!"