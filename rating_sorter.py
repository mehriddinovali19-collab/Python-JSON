import json
input_file = open("students.json", "r")
json01 = input_file.read()

data = json.loads(json01)
data.sort(key = lambda students: students['score'])

output_file = json.dumps(data, indent = 4)
f = open('rating.json', "w")
f.write(output_file)
