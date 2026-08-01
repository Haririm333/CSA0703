import random

def calculate_parity(binary_str):
    """Calculates even parity bit."""
    return '0' if binary_str.count('1') % 2 == 0 else '1'

def calculate_checksum(message):
    """Calculates a simple checksum by summing ASCII values."""
    return sum(ord(char) for char in message) % 256

def text_to_binary_with_parity(message):
    """Converts text to binary and appends an even parity bit."""
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    parity_bit = calculate_parity(binary_message)
    return binary_message + parity_bit

def introduce_noise(binary_str):
    """Randomly flips one bit in the string to simulate noise."""
    index = random.randint(0, len(binary_str) - 1)
    flipped_bit = '0' if binary_str[index] == '1' else '1'
    return binary_str[:index] + flipped_bit + binary_str[index+1:]

def check_parity(received_binary):
    """Checks if the received binary string passes even parity."""
    data = received_binary[:-1]
    received_parity = received_binary[-1]
    expected_parity = calculate_parity(data)
    return expected_parity == received_parity

# --- Simulation ---
messages = ["HELLO", "DATA", "NET", "CODE", "PACKET"]

print("--- Parity Check Simulation ---")
for msg in messages:
    print(f"\nOriginal Message: {msg}")
    encoded = text_to_binary_with_parity(msg)
    
    # Simulate transmission (corrupt ~100% for this test to show detection)
    received = introduce_noise(encoded) 
    
    if check_parity(received):
         print("Status: OK")
    else:
         print("Status: ERROR DETECTED (Parity mismatch)")

print("\n--- Checksum vs Parity comparison ---")
# For the README: Explain that parity only catches an ODD number of bit flips. 
# If 2 bits flip, parity fails to detect it. Checksums are slightly more robust for larger blocks of data!