import os
import xml.etree.ElementTree as ET

def parse_coverage(xml_path="coverage.xml"):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    line_rate = float(root.attrib.get("line-rate", 0))
    return round(line_rate * 100, 2)

def post_commit_status(coverage):
    token = os.environ["GITHUB_TOKEN"]
    sha = os.environ["GITHUB_SHA"]
    repo = os.environ["GITHUB_REPOSITORY"]

    description = f"Coverage: {coverage}%"
    state = "success" if coverage >= 80 else "failure"

    url = f"https://api.github.com/repos/{repo}/statuses/{sha}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "state": state,
        "description": description,
        "context": "code-coverage"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

if __name__ == "__main__":
    coverage = parse_coverage()
    post_commit_status(coverage)