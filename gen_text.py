types = ['farms', 'groceries', 'logging', 'textile', 'fishing', 'furniture', 'paper', 'motor', 'alcohol', 'meat', 'mining', 'boats', 'glass', 'plantations', 'explosives', 'silk', 'steel', 'tools', 'military']


schema = ''' country_invention_~_add:1 "[concept_invention_progress] towards ~"
 country_invention_~_add_desc:1 "Monthly increase or decrease in the $country_invention_~_add$""
'''

with open("output.txt", "w") as output_file:
    for t in types:
        output_file.write(schema.replace("~", t))