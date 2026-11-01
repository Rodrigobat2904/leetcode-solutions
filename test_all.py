import subprocess
import sys
from pathlib import Path

def main():
    problems_dir = Path(__file__).parent / "problems"
    solution_files = sorted(problems_dir.glob("*/solution.py"))
    
    print(f"Found {len(solution_files)} solution test suites.\n")
    failed = 0
    
    for solution_path in solution_files:
        problem_name = solution_path.parent.name
        print(f"Testing {problem_name}...", end=" ")
        result = subprocess.run([sys.executable, str(solution_path)], capture_output=True, text=True)
        if result.returncode == 0:
            print("PASSED")
        else:
            print("FAILED")
            print(result.stderr)
            failed += 1
            
    if failed == 0:
        print(f"\nAll {len(solution_files)} problems passed verification successfully!")
        sys.exit(0)
    else:
        print(f"\n{failed} problem(s) failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
