from qdrant_builder import qdrant_builder

datasets = [
    {"questions": "Who is the Dean of engineering department?", "command": "select dean from colleges where name = 'College of engineering';", "lang": "en"},
    {"questions": "کێ ڕاگری کۆلێژی ئەندازیاریە؟", "command": "select dean from colleges where name = 'College of engineering';", "lang": "ku"},
]

qdrant_builder(datasets)
