from time import sleep

def type_text(color: str, text: str, speed: float = 0.005) -> None:
  for char in text:
    # after every 65th character add "/n"
    if len(text[:text.index(char) + 1]) % 65 == 0:
      print()
    print(color + char, end="", flush=True)
    sleep(speed)
    