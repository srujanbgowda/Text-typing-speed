import time

text_to_type = "The quick brown fox jumps over the lazy dog"

print("Type the following text as fast as you can: ")
print(f"\n {text_to_type}\n")

input("Press Enter when your ready.. ")
start_time = time.time()
typed_text = input("Start typing: ")
end_time = time.time()

time_taken = end_time - start_time
words = len(typed_text.split())
speed_wpm = (words / time_taken) * 60

correct_chars = sum(1 for a,b in zip(text_to_type, typed_text) if a==b)
accuracy = (correct_chars / len(text_to_type)) * 100

print("\n ---Result-----")
print(f"Time taken: {round(time_taken,2)} seconds")
print(f"Speed: {round(speed_wpm,2)} words per minute (wpm)")
print(f"Accuracy: {round(accuracy,2)} %")