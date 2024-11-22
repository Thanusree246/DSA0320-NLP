import re

text = "The rain in Spain falls mainly on the plain. Spain is beautiful."

pattern = r"\b[Ss]\w*"

matches = re.findall(pattern, text)
print("Words starting with 'S' or 's':", matches)

search_result = re.search(r"Spain", text)
if search_result:
    print(f"'Spain' found at index {search_result.start()} to {search_result.end()}.")

replaced_text = re.sub(r"Spain", "Portugal", text)
print("Replaced text:", replaced_text)
