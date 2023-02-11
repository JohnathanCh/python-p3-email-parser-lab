# your code goes here!
import pdb
import re
class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails
    
    #----------------------My Solution--------------------------------
    def parse(self):
        pattern3 = r"([A-Za-z0-9]+[.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,})"
        regex = re.compile(pattern3)
        finded = regex.findall(self.emails)
        sorted_list = sorted(finded)
        return sorted_list
    
    #------------------------FI Solution--------------------------------
    # def parse(self):
    #     strings = re.split(r',|\s', self.emails)
        
    #     parsed_emails = set()
    #     for string in strings:
    #         if self.email_regex.fullmatch(string):
    #             parsed_emails.add(string)

    #     return sorted(list(parsed_emails))