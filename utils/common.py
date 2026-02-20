def generate_next_id(
    data:list,
    id_column: str
) -> int:
    '''
    Arguments:
    - data: List of data

    Return next ID value to assign.
    '''

    if not data:
        return 1
    return max([record[id_column] for record in data], default=0) + 1