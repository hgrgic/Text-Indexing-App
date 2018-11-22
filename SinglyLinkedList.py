class SLinkedList:
    def __init__(self):
        self.headval = None
        self.lastelement = None

    def __add__(self, new_node):

        if (self.headval is None):
            self.headval = new_node
            self.lastelement = new_node
        else:
            temp_last_element = self.lastelement
            temp_last_element.next_val = new_node
            self.lastelement = new_node

    def traverse_list(self):
        string_val = ""
        start_value = self.headval
        while start_value is not None:
            string_val += "->[" + str(start_value.article_num) + "," + str(start_value.occurrence_num) + "]"
            start_value = start_value.next_val
        return string_val


class SNode:
    def __init__(self, article_num=0, occurrence_num=0):
        self.article_num = article_num
        self.occurrence_num = occurrence_num
        self.next_val = None
