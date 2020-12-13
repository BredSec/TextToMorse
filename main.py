import json

running = True

with open("data.json") as f:
	data = json.load(f)

while running:
	ttm_mmt = input("would you like to use Text to Morse, or Morse to Text? [ttm/mtt]: ")

	if ttm_mmt.lower() == "ttm":
		morsestring = ""
		textstring = input("What would you like to translate into morse? : ")

		for char in textstring:
			morsestring += data["ttm"][char]
			morsestring += " "

		print(morsestring)
	elif ttm_mmt.lower() == "mtt":
		morsestring = input("What would you like to translate into text? : ")

		templetter = ""
		textstring = ""
		length = 0

		for char in morsestring:
			length += 1
			if char != " ":
				try:
					templetter += char
					if length - 1 == len(morsestring) - 1:
						textstring += data["mtt"][templetter]
						templetter = ""
				except:
					print("no")
			else:
				try:
					textstring += data["mtt"][templetter]
					templetter = ""
				except:
					print("invalid")

		print(textstring)