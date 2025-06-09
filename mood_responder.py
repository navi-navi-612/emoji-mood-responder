mood_dict = {
    "happy": ("😊", "Keep smiling! Your joy is contagious."),
    "sad": ("😢", "It's okay to feel down. Brighter days are ahead."),
    "angry": ("😠", "Take a deep breath. You’ve got this!"),
    "excited": ("🤩", "That's awesome! Keep riding the excitement!"),
    "tired": ("😴", "Get some rest. You deserve it."),
    "bored": ("😐", "Try something new — adventure awaits!")
}

# Step 4 & 5: Ask for user input and normalize it
user_mood = input("How are you feeling today? ").lower().strip()

# Step 6,7 & 8: Check mood and respond accordingly
if user_mood in mood_dict:
    emoji, message = mood_dict[user_mood]
    print(f"{emoji} {message}")
else:
    print("🤔 I'm not sure how you're feeling, but I hope you have a wonderful day!")