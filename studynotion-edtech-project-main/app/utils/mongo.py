from bson import ObjectId


def stringify_objectids(value):
    if isinstance(value, ObjectId):
        return str(value)
    if isinstance(value, list):
        return [stringify_objectids(item) for item in value]
    if isinstance(value, dict):
        return {key: stringify_objectids(val) for key, val in value.items()}
    return value


def with_string_id(doc: dict | None) -> dict | None:
    if doc is None:
        return None
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return stringify_objectids(doc)
