import CodeMap
import FileHandler
from lxml import etree
from lxml import objectify

import Util

INPUT = "input"
OUTPUT = "output"

column_name = "underwritingDecision"

match_rule_tag = lambda element: "rule" in element.tag
match_input_tag = lambda element: "input" in element.tag
match_output_tag = lambda element: "output" in element.tag
match_column_name = lambda element: element.attrib["name"] == column_name

output_columns = ["uwDecision", "uwDecisionCode", "uwDecisionStatus", "uwDecisionAggregateCode"]


def get_code(key):
    return CodeMap.CODE_MAP[key]


def get_output_entry(text):
    id = Util.generate_random_string(32)
    element_str = f'<outputEntry id="{id}"><text>"{text}"</text></outputEntry>'
    element = objectify.fromstring(element_str)
    return element


def add_output_column(output_columns, root):
    last_output = root.decision.decisionTable.output.getprevious()
    output_columns.reverse()
    for col in output_columns:
        print(f"adding column {col}")
        id = Util.generate_random_string(32)
        output_str = f'<output id="{id}" name="{col}" typeRef="string" />'
        output = objectify.fromstring(output_str)
        last_output.addnext(output)


def get_all_children(path, root):
    file_content = FileHandler.read_file(path)
    root = objectify.fromstring(file_content)
    child_elements = root.decision.decisionTable.getchildren()
    return child_elements


def calculate_column_number(elements):
    input_output = Util.remove_objects_with_condition(elements, match_rule_tag)
    return Util.get_index_of_element(input_output, match_column_name)


def get_rules(all_child_elements):
    rules = Util.remove_objects_with_condition(all_child_elements, match_output_tag)
    return Util.remove_objects_with_condition(rules, match_input_tag)



def get_code_map(rule, column_number):
    uw_decision_col = rule.getchildren()[column_number]
    unsanitized_key = uw_decision_col.getchildren()[0].pyval
    key = unsanitized_key.replace("\"", "") if "\"" in unsanitized_key else unsanitized_key
    key = key.replace("\'", "") if "\'" in key else key
    key = key.replace("\n", "")
    key = key.strip()
    code = CodeMap.get_code(key)
    return code


def process_file(file_path):
    file_content = FileHandler.read_file(file_path)
    file_content = remove_encoding(file_content)
    root = objectify.fromstring(file_content)
    all_children = root.decision.decisionTable.getchildren()

    column_number = calculate_column_number(all_children)
    rules = get_rules(all_children)

    for rule in rules:
        code = get_code_map(rule, column_number)

        uwDecision = get_output_entry(code[output_columns[0]])
        uwDecisionCode = get_output_entry(code[output_columns[1]])
        uwDecisionStatusCode = get_output_entry(code[output_columns[2]])
        uwDecisionAggregateCode = get_output_entry(code[output_columns[3]])

        output = rule.outputEntry
        output.addprevious(uwDecision)
        output.addprevious(uwDecisionCode)
        output.addprevious(uwDecisionStatusCode)
        output.addprevious(uwDecisionAggregateCode)

    add_output_column(output_columns, root)
    xml_string = etree.tostring(root, pretty_print=True, encoding="utf-8").decode()

    path = OUTPUT + file_path
    Util.write_to_file(path, xml_string)


def remove_encoding(content):
    content = content.replace('encoding="utf-8"', '')
    return content.replace('encoding="UTF-8"', '')


if __name__ == '__main__':
    # files = Util.list_files(INPUT)
    # for file in files:
    #     process_file(file)
    file_path = "input/BMI_Rules.dmn"
    process_file(file_path)
