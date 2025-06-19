import subprocess
import os

def git_commit_and_push(working_directory, commit_message):
    try:
        cmds = [
            ["git", "add", "-A"],
            ["git", "commit", "-m", commit_message],
            ["git", "push"]
        ]
        for cmd in cmds:
            result = subprocess.run(cmd, cwd=working_directory, capture_output=True, text=True)
            if result.returncode != 0:
                return (
                    f"❌ Git command failed: {' '.join(cmd)}\n"
                    f"STDOUT:\n{result.stdout.strip()}\n"
                    f"STDERR:\n{result.stderr.strip()}\n"
                    f"💡 Tip: Check 'git status' manually to verify staged changes."
                )
        return "✅ Successfully committed and pushed changes to GitHub."
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
