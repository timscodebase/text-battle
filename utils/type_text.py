import time

def type_text(color: str, text: str, speed: float = 0.005) -> None:
  for char in text:
    print(color | f"{char}", end="", flush=True)
    time.sleep(speed)