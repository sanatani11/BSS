import random
def main():
    fname = "Raushan" 
    lname = "Ranjan"
    admission_number = "21JE0751" 

    print(f"\nWelcome to {fname} {lname}'s Fortune Teller ({admission_number})\n")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            f"You're on a roll {fname} — don’t stop now!",
            f"Good vibes ahead {fname}. Keep riding that wave, dear!"
        ],
        "sad": [
            "It's okay to not be okay. Brighter days are coming.",
            "The clouds will clear soon. Hang in there."
        ],
        "neutral": [
            "Still waters run deep. Something surprising is coming.",
            "No chaos = more clarity. Use this moment."
        ],
        "stressed":[
            "Streesing won't help at all, keep calm",
            "Stressing is the mother of all problems, keep calm"
        ]
    }

    if mood in fortunes:
        message = random.choice(fortunes[mood])
        print(f"\nYour fortune: {message} \n")
    else:
        print("\nHmm, I don’t know that mood. Try happy/sad/neutral/stressed.\n")


if __name__ == "__main__":
    main()