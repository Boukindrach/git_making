import sys
import os
import subprocess
import zlib


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    if command == "cat-file":
        result = subprocess.run(
            ['git', 'hash-object', '-w', 'test.txt'],
            capture_output=True,
            text=True                 
        )
        hash_value = sys.argv[3]
        with open(f".git/objects/{hash_value[:2]}/{hash_value[2:]}", "rb") as f:
            compressed = f.read()
            decompressed = zlib.decompress(compressed)
        s = decompressed.decode('utf-8')
        for i in range(5, len(s)):
            if s[i] >= 'a' and s[i] <= 'z':
                print(s[i:], end="")
                return


    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
