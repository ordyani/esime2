import datetime
import sys

def main():
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    print(f"C2AI test app started at {stamp}")
    print(f"Python version: {sys.version}")
    result = sum(range(1, 101))  # trivial work so there's real output
    print(f"Computed sum 1..100 = {result}")
    with open("deploy-proof.txt", "w") as f:
        f.write(f"Deployed and ran at {stamp}\nResult: {result}\n")
    print("Wrote deploy-proof.txt")
    print("C2AI test app finished OK")

if __name__ == "__main__":
    main()
