import subprocess
import pandas as pd
import pexpect
import time

directory_name = "Brown100"
subprocess.run(["cd", directory_name])
urls = pd.read_csv("problem_urls.csv")["Problem Link"].tolist()

for url in urls:
    # Extract contest_id and problem_id from url
    contest_id = url.split("/")[-1][:-2]
    problem_id = url[-1]
    
    # Create a new problem in the contest
    child = pexpect.spawn(f"acc new {contest_id}")
    time.sleep(1)
    child.sendline(" ")
    for alphabet in range(ord(problem_id)-ord('a')):
        child.sendline("\x1b[B")
    child.sendline(" ")
    child.sendline("\n")
    
    # Download the test cases
    subprocess.run(["oj", "dl", url, "--directory", f"{contest_id}/{url[-1]}/tests"])

