print("🌞 Tanning Safety Tracker 🎀")
print("Here are some tips to stay safe in the sun:")
print("- Wear sunscreen!")
print("- Don't stay out too long!")
print("- Drink water!")
print("- Avoid tanning from 10 AM to 4 PM!")
print("------------------------------------")

tanning_times = []

while True:
    user_input = input("Enter how many minutes you tanned (or type 'done'): ")
    if user_input.lower() == "done":
        break
    if user_input.isdigit():
        minutes = int(user_input)
        if minutes > 0:
            tanning_times.append(minutes)
        else:
            print("Please enter a number greater than 0.")
    else:
        print("Please enter a valid number or 'done'.")

print("------------------------------------")
print("You have tanned " + str(len(tanning_times)) + " times.")
print("Total tanning time: " + str(sum(tanning_times)) + " minutes")
print("------------------------------------")

print("🧴 Safe Tanning Time Calculator 🏖️")

def get_safe_tanning_time(skin, uv):
    skin_type = skin.lower()
    if skin_type == "fair":
        return 10
    elif skin_type == "medium":
        return 20
    elif skin_type == "dark":
        return 30
    else:
        return None

while True:
    skin_type = input("Enter your skin type (fair, medium, dark): ")
    if skin_type.lower() in ["fair", "medium", "dark"]:
        break
    else:
        print("Please enter fair, medium, or dark.")

while True:
    uv_input = input("Enter today's UV index (1 to 10): ")
    if uv_input.isdigit():
        uv_index = int(uv_input)
        if uv_index >= 1 and uv_index <= 10:
            break
        else:
            print("The number must be from 1 to 10.")
    else:
        print("Please enter a valid number.")

safe_minutes = get_safe_tanning_time(skin_type, uv_index)
if safe_minutes is not None:
    print("Based on your skin type and UV index, you should tan for about " + str(safe_minutes) + " minutes.")
    print("✅ Stay safe and enjoy the sun responsibly! 👙🧴")
else:
    print("Sorry, we couldn't calculate a safe tanning time.")


