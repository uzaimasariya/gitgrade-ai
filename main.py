import requests

repo_url = input("Paste GitHub repository link: ")

api_url = repo_url.replace(
    "https://github.com/",
    "https://api.github.com/repos/"
)

data = requests.get(api_url).json()

score = 0
roadmap = []

if data["language"]:
    score += 30
else:
    roadmap.append("Add programming language")

if data["stargazers_count"] > 0:
    score += 20
else:
    roadmap.append("Make project more useful")

score += 30  # basic effort points

print("\nScore:", score, "/100")
if score >= 70:
    print("Summary: Good project with basic structure.")
else:
    print("Summary: Project needs improvement.")
print("\nRoadmap:")
if roadmap:
    for step in roadmap:
        print("-", step)
else:
    print("- Keep improving and add advanced features")
