

def assign_object_from_dict(target_class, source_dict: dict) -> object:

    for key in source_dict.keys():
        setattr(target_class, key, source_dict[key])

    return target_class

def assign_dict_from_object(source_class) -> dict:

    result = {}


    property_exclusion_filter = [
        '_sa_registry',
        '_is_protocol',
        '_sa_class_manager',
        '_sa_instance_state',
        'metadata',
        'registry'
    ]

    members = [attr for attr in dir(source_class) if not attr.startswith("__") and not callable(getattr(source_class, attr))]

    for member in members:
        if member not in property_exclusion_filter:
            result[member] = getattr(source_class, member)

    return result
