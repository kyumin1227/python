import struct

foo = 3.18

foo_byte = struct.pack("f", foo)
print(f"[foo_byte] : {foo_byte}")

bar = 1024

print(f"[bar] : {bar}, [data type of bar] : {type(bar)}")

bar_byte = bar.to_bytes(4, "little")

print(f"[bar_byte] : {bar_byte}, [data type of bar_byte] : {type(bar_byte)}")