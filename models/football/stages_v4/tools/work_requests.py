"""Select only newly changed requests; code-only pushes never acquire a slate."""
import json
import os
import subprocess
from pathlib import Path

PREFIX = "models/football/stages_v4/acquisition_requests/"


def validated_path(name, prefix=PREFIX):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts or not name.startswith(prefix) or path.suffix != ".json" or not path.is_file() or path.is_symlink():
        raise ValueError("invalid repository request/source path: " + name)
    return name


def select(event, event_name):
    if event_name == "workflow_dispatch":
        inputs = event.get("inputs", {})
        request = validated_path(inputs.get("request_file", ""))
        source = inputs.get("source_file") or ""
        if source:
            validated_path(source, "models/football/stages_v4/recovery/")
        return [{"request": request, "source": source}]
    if event_name != "push":
        return []
    before, after = event.get("before", ""), event.get("after", "")
    # A new branch must not replay the entire repository's request history.
    if not before.strip("0"):
        return []
    for sha in (before, after):
        if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            raise ValueError("invalid event commit SHA")
    changed = subprocess.check_output(["git", "diff", "--name-only", "--diff-filter=AM", before, after, "--", PREFIX], text=True)
    return [{"request": validated_path(name), "source": ""} for name in changed.splitlines() if name.endswith(".json")]


if __name__ == "__main__":
    result = select(json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text()), os.environ["GITHUB_EVENT_NAME"])
    with open(os.environ["GITHUB_OUTPUT"], "a") as output:
        output.write("matrix=" + json.dumps({"include": result}) + "\n")
        output.write("has_requests=" + str(bool(result)).lower() + "\n")
