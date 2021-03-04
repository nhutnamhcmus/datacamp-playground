def convert_to_int(number_with_commas):
    return number_with_commas.replace(",", "")


def row_to_list(row):
    row = row.rstrip("\n")
    separated_entries = row.split("\t")
    if len(separated_entries) == 2 and "" not in separated_entries:
        return separated_entries
    return None
