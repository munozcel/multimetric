json_data = {
  "files": {
    "/Users/munozcel/Documents/GitHub/multimetric/egon.py": {
      "comment_ratio": 24.204119850187265,
      "cyclomatic_complexity": 4,
      "fanout_external": 5,
      "fanout_internal": 0,
      "halstead_bugprop": 0.7221461985360021,
      "halstead_difficulty": 25.363636363636367,
      "halstead_effort": 54948.76074314853,
      "halstead_timerequired": 3052.7089301749184,
      "halstead_volume": 2166.4385956080064,
      "lang": [
        "Python"
      ],
      "loc": 63,
      "operands_sum": 155,
      "operands_uniq": 55,
      "operators_sum": 195,
      "operators_uniq": 18
    }
  },
  "overall": {
    "comment_ratio": 24.204119850187265,
    "cyclomatic_complexity": 4,
    "fanout_external": 5,
    "fanout_internal": 0,
    "halstead_bugprop": 0.7221461985360021,
    "halstead_difficulty": 25.363636363636367,
    "halstead_effort": 54948.76074314853,
    "halstead_timerequired": 3052.7089301749184,
    "halstead_volume": 2166.4385956080064,
    "loc": 63,
    "maintainability_index": 63.02084996228787,
    "operands_sum": 155,
    "operands_uniq": 55,
    "operators_sum": 195,
    "operators_uniq": 18,
    "pylint": 100.0,
    "tiobe": 93.80733944954129,
    "tiobe_compiler": 100.0,
    "tiobe_complexity": 58.71559633027523,
    "tiobe_coverage": 100.0,
    "tiobe_duplication": 100.0,
    "tiobe_fanout": 100.0,
    "tiobe_functional": 100.0,
    "tiobe_security": 100.0,
    "tiobe_standard": 100.0
  },
  "stats": {
    "max": {
      "comment_ratio": 24.204119850187265,
      "cyclomatic_complexity": 4,
      "fanout_external": 5,
      "fanout_internal": 0,
      "halstead_bugprop": 0.7221461985360021,
      "halstead_difficulty": 25.363636363636367,
      "halstead_effort": 54948.76074314853,
      "halstead_timerequired": 3052.7089301749184,
      "halstead_volume": 2166.4385956080064,
      "loc": 63,
      "operands_sum": 155,
      "operands_uniq": 55,
      "operators_sum": 195,
      "operators_uniq": 18
    },
    "mean": {
      "comment_ratio": 24.204119850187265,
      "cyclomatic_complexity": 4,
      "fanout_external": 5,
      "fanout_internal": 0,
      "halstead_bugprop": 0.7221461985360021,
      "halstead_difficulty": 25.363636363636367,
      "halstead_effort": 54948.76074314853,
      "halstead_timerequired": 3052.7089301749184,
      "halstead_volume": 2166.4385956080064,
      "loc": 63,
      "operands_sum": 155,
      "operands_uniq": 55,
      "operators_sum": 195,
      "operators_uniq": 18
    },
    "median": {
      "comment_ratio": 24.204119850187265,
      "cyclomatic_complexity": 4,
      "fanout_external": 5,
      "fanout_internal": 0,
      "halstead_bugprop": 0.7221461985360021,
      "halstead_difficulty": 25.363636363636367,
      "halstead_effort": 54948.76074314853,
      "halstead_timerequired": 3052.7089301749184,
      "halstead_volume": 2166.4385956080064,
      "loc": 63,
      "operands_sum": 155,
      "operands_uniq": 55,
      "operators_sum": 195,
      "operators_uniq": 18
    },
    "min": {
      "comment_ratio": 24.204119850187265,
      "cyclomatic_complexity": 4,
      "fanout_external": 5,
      "fanout_internal": 0,
      "halstead_bugprop": 0.7221461985360021,
      "halstead_difficulty": 25.363636363636367,
      "halstead_effort": 54948.76074314853,
      "halstead_timerequired": 3052.7089301749184,
      "halstead_volume": 2166.4385956080064,
      "loc": 63,
      "operands_sum": 155,
      "operands_uniq": 55,
      "operators_sum": 195,
      "operators_uniq": 18
    }
  }
}

filtered_data = []
overall_data = {
  "comment_ratio": json_data["overall"]["comment_ratio"],
  "loc": json_data["overall"]["loc"],
  "cyclomatic_complexity": json_data["overall"]["cyclomatic_complexity"]
}
filtered_data.append(overall_data)
print(filtered_data)

