#Advanced Party manager

guests = {}

guests["Alice"] = (28, "alice@email.com")
guests["Bob"] = (35, "bob@email.com")
guests["Charlie"] = (30, "charlie@email.com")

guests["David"] = (22, "david@email.com")
del guests["Bob"]

def get_guest_info(guest_name):
    if guest_name in guests:
        age, email = guests[guest_name]
        return f"{guest_name} (Age: {age}) is coming to the party! Email: {email}"
    else:
        return f"{guest_name} is not on the guest list."

def count_guests():
    return f"Total guests: {len(guests)}"

def add_guest():
    name = input("Enter guest name: ")
    if name in guests:
        choice = input("Guest already exists. Update details? (yes/no): ").strip().lower()
        if choice != "yes":
            return "Guest not updated."
    age = int(input("Enter guest age: "))
    email = input("Enter guest email: ")
    guests[name] = (age, email)
    return f"{name} added/updated successfully!"

def display_sorted_guests():
    sorted_guests = sorted(guests.items(), key=lambda x: x[1][0])
    for name, (age, email) in sorted_guests:
        print(f"{name}: Age {age}, Email: {email}")

if __name__ == "__main__":
    print(get_guest_info("Alice"))
    print(count_guests())
    print(add_guest())
    display_sorted_guests()