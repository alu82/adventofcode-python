import os
import time
import re

rule_8 = "42 | 42 8"
rule_11 = "42 31 | 42 11 31"

class Rule:
    def __init__(self, rule_text, n_r11=1):
        self.rule_text = rule_text
        self.n_r11 = n_r11
    
    def to_regex(self, rules):
        if self.rule_text == rule_8:
            return rules["42"].to_regex(rules) + "+"
        elif self.rule_text == rule_11:
            occ = "{" + str(self.n_r11) + "}"
            return rules["42"].to_regex(rules)+ occ + rules["31"].to_regex(rules) + occ
        elif "\"" in self.rule_text:
            return self.rule_text.replace("\"", "")
        elif self.rule_text.isdigit():
            return rules[self.rule_text].to_regex(rules)
        elif " | " in self.rule_text:
            r1, r2 = self.rule_text.split(" | ")
            return "(" + Rule(r1).to_regex(rules) + "|" + Rule(r2).to_regex(rules) + ")"
        else:
            reg = ""
            for rx in self.rule_text.split(" "):
                reg += Rule(rx).to_regex(rules)
            return reg 

def solve_1(raw_rules, messages):
    rules = get_rules(raw_rules)
    regex = "^"+rules["0"].to_regex(rules)+"$"
    return len([m for m in messages if re.match(regex,m)])

def solve_2(raw_rules, messages):
    rules = get_rules(raw_rules)
    rules["8"] = Rule(rule_8)
    rules["11"] = Rule(rule_11)
    sum_ = 0
    for n_r11 in range(1,20):
        rules["11"].n_r11 = n_r11
        regex = "^"+rules["0"].to_regex(rules)+"$"
        sum_ += len([m for m in messages if re.match(regex,m)])
        # print("current sum", sum_)
    return sum_

def get_rules(raw_rules):
    rules = dict()
    for l,r in [rr.split(":") for rr in raw_rules]:
        rules[l] = Rule(r.strip())
    return rules

with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [block.splitlines() for block in myInput.read().split("\n\n")]
    print("part1", solve_1(input[0], input[1]))
    print("part2", solve_2(input[0], input[1]))
    print("--- Execution time %s s ---" % (time.time() - start_time))