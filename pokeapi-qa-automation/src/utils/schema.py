pokemon_schema = {
    "type": "object",
    "required": ["id", "name", "abilities", "moves", "stats"],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1},
        "abilities": {"type": "array"},
        "moves": {"type": "array"},
        "stats": {"type": "array"},
    },
    "additionalProperties": True
}
