# src/rules.py

EVALUATION_RULES = {
    "exits": {
        "description": "Evacuation plan should reference multiple exits",
        "keywords": ["exit", "stairwell"],
        "min_count": 2
    },
    "assembly_point": {
        "description": "Evacuation plan should clearly define an assembly point",
        "keywords": ["assembly", "meeting point", "gather"],
        "min_count": 1
    },
    "accessibility": {
        "description": "Evacuation plan should address accessibility needs",
        "keywords": ["accessible", "disability", "wheelchair", "assist"],
        "min_count": 1
    },
    "clarity": {
        "description": "Evacuation instructions should be clear and directive",
        "keywords": ["follow", "proceed", "use", "do not"],
        "min_count": 3
    }
}
