def get_names_from_templates(templates):
    names = []

    for i in range(len(templates)):
        name = templates[i]["name"]
        print(f"{i + 1}: {name}")
        names.append(name)

    return names


def print_schedule(template):
    print(f'Template `{template["name"]}`')

    for week, days in template["schedule"].items():
        print(f"`{week}`: {days}")

