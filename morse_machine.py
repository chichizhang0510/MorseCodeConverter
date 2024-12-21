import pandas as pd


class MorseMachine:
    def __init__(self):
        self.input = ""
        self.output = ""
        self.store = []
        self.bracket_num = 0
        self.rule_file = "morse_rule.csv"
        self.symbol = [
            '.', ',', '?', "'",
            '!', ':', '()', '&',
            ':', ';', '=', '+',
            '-', '_', '"', '$', '@'
        ]

    def get_input(self, message):
        self.input = message

    def break_message(self, op_type):
        """
        :param op_type: "en" or "de"
        """
        if op_type == "en":
            break_list = self.input.upper().split(" ")
            for i in break_list:
                if i[0] in self.symbol or i[-1] in self.symbol:
                    if i[0] in self.symbol and i[-1] not in self.symbol:
                        self.store.append(i[0])
                        self.store.append(i[1:])
                    if i[0] not in self.symbol and i[-1] in self.symbol:
                        self.store.append(i[:-1])
                        self.store.append(i[-1])
                    if i[0] in self.symbol and i[-1] in self.symbol:
                        self.store.append(i[0])
                        self.store.append(i[1:-1])
                        self.store.append(i[-1])
                else:
                    self.store.append(i)
        else:
            break_list = self.input.split("   ")
            for i in break_list:
                single_i = i.split(" ")
                self.store.append(single_i)

    def single_encryption(self, char):
        df_rule = pd.read_csv(self.rule_file)
        code = df_rule[df_rule['humanInput'] == char]['morseCode'].iloc[0]
        return code

    def single_decryption(self, code):
        df_rule = pd.read_csv(self.rule_file)
        char = df_rule[df_rule['morseCode'] == code]['humanInput'].iloc[0]
        if char == "()":
            self.bracket_num += 1
            char = "(" if self.bracket_num // 2 == 1 else ")"
        return char

    def encryption(self):
        all_result = []
        self.break_message("en")
        for i in self.store:
            single_result = []
            for j in i:
                single_result.append(self.single_encryption(j))
            all_result.append(" ".join(single_result))
        self.output = "   ".join(all_result)
        return self.output

    def decryption(self):
        all_result = []
        self.break_message("de")
        for i in self.store:
            single_result = []
            for j in i:
                single_result.append(self.single_decryption(j))
            all_result.append("".join(single_result))

        self.output = " ".join(all_result)
        return self.output

    def restart(self):
        self.input = ""
        self.output = ""
        self.store = []
        self.bracket_num = 0