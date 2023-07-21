class FundInformation(object):
    def __init__(self):
        pass

    def get_information_from_web(self, find_statement):
        information_list = []

        for information_item in find_statement:
            key_and_value = {
                information_item.p.getText(): information_item.b.getText()   
            }

            information_list.append(key_and_value)

        return information_list