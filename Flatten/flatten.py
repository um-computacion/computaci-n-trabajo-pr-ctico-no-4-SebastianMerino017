def flatten_list(nested_list):
    flattened = []
    
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        elif isinstance(item, tuple):
            flattened.extend(flatten_list(list(item)))
        elif isinstance(item, dict):
            for key in item:
                flattened.append(key)
                flattened.append(item[key])
        else:
            flattened.append(item)
    
    return flattened