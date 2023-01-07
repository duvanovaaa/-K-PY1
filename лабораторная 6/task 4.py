import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_, delimiter=',', new_line='\n') -> list[dict]:
    with open(file_) as fun:
        data = []
        for index, line in enumerate(fun):
            lines = line.strip(new_line).split(delimiter)
            if index == 0:
                titles = lines
                continue

            data.append({})

            for i, _ in enumerate(titles):
                data[-1][titles[i]] = lines[i]
    return data

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


