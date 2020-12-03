sample = []
valid_passwords = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        sample.append(line.rstrip())

#2-5 j: bjjjj

# def get_compliance(input):
#     process_input = input.split()
#     repeats = process_input[0]
#     limits = repeats.split('-')
#     lower_limit = int(limits[0])
#     upper_limit = int(limits[1])
#     alphabet = process_input[1][0]
#     input_string = process_input[2]
#     count = 0
#     for i in input_string:
#         if i == alphabet:
#             count += 1
#     if count >= lower_limit and count <=  upper_limit:
#         return True
#     else:
#         return False


def get_compliance_2(input):
    process_input = input.split()
    repeats = process_input[0]
    limits = repeats.split('-')
    position_one = int(limits[0])
    position_two = int(limits[1])
    alphabet = process_input[1][0]
    input_string = process_input[2]
    count = 0
    if input_string[position_one-1] == alphabet or input_string[position_two-1] == alphabet:
        count += 1
    if count == 1:
        return True
    else: 
        return False


for i in sample:
    if get_compliance_2(i):
        valid_passwords += 1

print(valid_passwords)

    




