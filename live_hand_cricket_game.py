import random
import time

print("🏏 --- WELCOME TO PYTHON HAND CRICKET --- 🏏\n")
print("Rules: Choose a number from 1 to 6. If your number matches the computer's, you are OUT!")

# --- BATTING PHASE ---
user_score = 0
print("\n🔥 Aap ki Batting Shuru Hotii Hai!")

while True:
    try:
        user_choice = int(input("Apna number dalein (1-6): "))
        if user_choice < 1 or user_choice > 6:
            print("⚠️ Sirf 1 se 6 tak ka number likhein!")
            continue
    except ValueError:
        print("⚠️ Valid number likhein!")
        continue

    comp_choice = random.randint(1, 6)
    print(f"🤖 Computer ne dikhaya: {comp_choice}")

    if user_choice == comp_choice:
        print(f"❌ OUTTT!!! Aap ka Total Score: {user_score} runs.")
        break
    else:
        user_score += user_choice
        print(f"✅ Safe! Aap ka Score: {user_score}")

# --- BOWLING PHASE ---
comp_score = 0
target = user_score + 1
print(f"\n🎯 Target: {target} runs. Ab aap ki Bowling hai!")

while comp_score < target:
    try:
        user_choice = int(input("Bowling karein (1-6 dikhayein): "))
        if user_choice < 1 or user_choice > 6:
            print("⚠️ Sirf 1 se 6 tak ka number likhein!")
            continue
    except ValueError:
        print("⚠️ Valid number likhein!")
        continue

    comp_choice = random.randint(1, 6)
    print(f"🤖 Computer ne mara: {comp_choice}")

    if user_choice == comp_choice:
        print(f"☝️ WICKET!!! Computer OUT ho gaya!")
        break
    else:
        comp_score += comp_choice
        print(f"🏏 Computer Score: {comp_score} / Target: {target}")

# --- RESULT ---
print("\n📊 --- MATCH RESULT ---")
if comp_score >= target:
    print("😭 Computer Jeet Gaya! Aap Match Haar Gaye.")
elif user_score > comp_score:
    print("🎉 MUBARAK HO! Aap Jeet Gaye!")
else:
    print("🤝 Match Draw Ho Gaya!")
