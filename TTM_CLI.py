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
			try:
				morsestring += data["ttm"][char]
				morsestring += " "
			except:
				print("Error: Invalid Character")

		print(morsestring)
	elif ttm_mmt.lower() == "mtt":
		morsestring = input("What would you like to translate into text? : ")

		while morsestring[-1] == " ":
			morsestring = morsestring[:-1]

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
					print("Error: Invalid Character")
			else:
				try:
					textstring += data["mtt"][templetter]
					templetter = ""
				except:
					print("Error: Invalid Character")

		print(textstring)
