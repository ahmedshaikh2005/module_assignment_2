def sleep_tracker(hours):
 return f'{hours} hours sleep is better for health '
hours = int(input("Enter your sleeping hours: "))


if hours < 8:
    print( f"{hours} hours of sleep is not enough. You are risking your health. Aim for at least sleep for 8 hours.")
else:
    print("You are doing great.")

