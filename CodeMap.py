data = [
    ['Accept', 'SYMUWDC01', 'Accept', 'SYMUWDC0101000102'],
    ['Accept', 'SYMUWDC01', 'Accept with same terms', 'SYMUWDC0101000102'],

    ['Accept', 'SYMUWDC01', 'Accept with exclusion', 'SYMUWDC0102000202'],
    ['Accept', 'SYMUWDC01', 'Accept with loading', 'SYMUWDC0102000302'],
    ['Accept', 'SYMUWDC01', 'Accept with loading and exclusion', 'SYMUWDC0102000402'],
    ['Accept', 'SYMUWDC01', 'Accept with special condition', 'SYMUWDC0102000502'],
    ['Accept', 'SYMUWDC01', 'Accepted with loading and special condition', 'SYMUWDC0102000602'],
    ['WIP', 'SYMUWDC02', 'Refer to tele Underwriter', 'SYMUWDC0202000402'],
    ['WIP', 'SYMUWDC02', 'Refer to CMO', 'SYMUWDC0202000502'],
    ['WIP', 'SYMUWDC02', 'Refer to Sr. Underwriter', 'SYMUWDC0202000602'],
    ['WIP', 'SYMUWDC02', 'Refer to underwriter', 'SYMUWDC0202000702'],
    ['WIP', 'SYMUWDC02', 'Refer to Head Underwriter', 'SYMUWDC0202000802'],
    ['WIP', 'SYMUWDC02', 'PPHC', 'SYMUWDC0202000102'],
    ['WIP', 'SYMUWDC02', 'Add Info', 'SYMUWDC0202000202'],
    ['WIP', 'SYMUWDC02', 'PPHC+Add Info', 'SYMUWDC0202000302'],
    ['Defer', 'SYMUWDC03', 'Deferment for 6 months', 'SYMUWDC0302000102'],
    ['Defer', 'SYMUWDC03', 'Defer - 6 months', 'SYMUWDC0302000102'],

    ['Defer', 'SYMUWDC03', 'Deferment for 12 months', 'SYMUWDC0302000202'],
    ['Defer', 'SYMUWDC03', 'Defer - 12 months', 'SYMUWDC0302000202'],

    ['Defer', 'SYMUWDC03', 'Deferment till fully investigated and treated', 'SYMUWDC0302000302'],
    ['Defer', 'SYMUWDC03', 'Defer - till further investigation and treatment', 'SYMUWDC0302000302'],

    ['Reject', 'SYMUWDC04', 'Reject', 'SYMUWDC0402000102']
]

CODE_MAP = {}

for row in data:
    uw_decision = row[0]
    uw_decision_code = row[1]
    uw_decision_status = row[2]
    uw_decision_aggregate_code = row[3]

    CODE_MAP[uw_decision_status] = {
        'uwDecision': uw_decision,
        'uwDecisionCode': uw_decision_code,
        'uwDecisionStatus': uw_decision_status,
        'uwDecisionAggregateCode': uw_decision_aggregate_code
    }


def get_value_case_insensitive(dictionary, key):
    # Convert the key to lowercase
    lowercase_key = key.lower()

    # Iterate over the dictionary keys
    for dict_key in dictionary.keys():
        # If the lowercase key matches a lowercase dictionary key, return the corresponding value
        if dict_key.lower() == lowercase_key:
            return dictionary[dict_key]

    # If no match is found, return None or raise an exception
    return None  # or raise KeyError("Key not found")


def get_code(key):
    lowercase_key = key.lower()
    for dict_key in CODE_MAP.keys():
        # If the lowercase key matches a lowercase dictionary key, return the corresponding value
        if dict_key.lower() == lowercase_key:
            return CODE_MAP[dict_key]
    else:
        return {
            'uwDecision': "",
            'uwDecisionCode': "",
            'uwDecisionStatus': "",
            'uwDecisionAggregateCode': ""
        }
# Example usage:
# status = 'Accept'
# if status in CODE_MAP:
#     decision = CODE_MAP[status]
#     print(f"uwDecision: {decision['uwDecision']}")
#     print(f"uwDecisionCode: {decision['uwDecisionCode']}")
#     print(f"uwDecisionStatusCode: {decision['uwDecisionStatusCode']}")
#     print(f"uwDecisionAggregateCode: {decision['uwDecisionAggregateCode']}")
