from validator_collection import validators

address = input("e-mail address: ").strip()

try:
    emailValid = validators.email(address)
    print("valid")
except ValueError:
    print("Invalid")