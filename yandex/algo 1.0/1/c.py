v_phone = input()
phone_book = [input(), input(), input()]

def parse_phone(phone):
    new_phone = "".join([c for c in phone if c.isdigit()])
    if len(new_phone) == 7:
        new_phone = "8495" + new_phone
    return new_phone[1:] 

v_phone = parse_phone(v_phone)

new_phones = ['YES' if parse_phone(phone) == v_phone else 'NO' for phone in phone_book]

for res in new_phones:
    print(res)