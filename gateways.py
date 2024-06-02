import time
import requests

class Gateways:

	def __init__(self, gateway_name, card = ''):
		if gateway_name == None:
			self.gateways = 'Not Defined'
		self.gateway_name = gateway_name
		self.card = card
		self.time = time.perf_counter()

	def loading(self, progress = 10):
		load = ''
		for i in range(int(progress * 10 / 100)):
			load += '+'
		return load

	def initial_progress(self, progress = 10):
		return f"""<b>⎚ Stripe | Auth {self.gateway_name}
Card: <code>{self.card}</code>
Progress 🟠 {self.time_taken()}(s)</b>"""

	def finish_progress(self, message_error, code_error = False):
		info = self.get_bin_info()

		if code_error == False:
			code_error = ''
		else:
			code_error = f'{code_error}'

		return f"""
<b>⎚ Stripe | Auth {self.gateway_name}

ϟ 𝑪𝒂𝒓𝒅: <code>{self.card}</code>
ϟ 𝐒𝐭𝐚𝐭𝐮𝐬: <b>{code_error}</b>
ϟ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>{message_error}</b>
ϟ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>{self.gateway_name}</code>
━━━━━━━━━🤍🕊
ϟ 𝐏𝐫𝐨𝐱𝐲 : Live!✅
ϟ 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧: <b>{self.time_taken()} (s)s</b>
━━━━━━━━━🤍🕊
ϟ『𝘋𝘦𝘝 ↯』: <b><a href="tg://resolve?domain=Was_FaReS">ϟ 𝐅𝐚𝐑𝐞𝐒 ϟ</a></b></b>
"""

	def mass_progress(self, message_error):
		return f"""<b>
ϟ 𝑪𝒂𝒓𝒅: <code>{self.card}</code>
ϟ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {message_error}
ϟ 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧: <code>{self.time_taken()} (s)</code>
━━━━━━</b>"""



	def get_bin_info(self):

		try:
			bin_code = self.card[:6]
			bin_data = requests.get(f"https://bin-api-dragon.ga/bin/api/{bin_code}").json()["data"]
			vendor   = bin_data["vendor"]
			type     = bin_data["type"]
			level    = bin_data["level"]
			country  = bin_data["country"]
			bank     = bin_data["bank"]
			countryInfo = bin_data["countryInfo"]
			name        = countryInfo["name"]
			codea       = countryInfo["code"]
			emoji       = countryInfo["emoji"]
			
			return bin_code, vendor, type, level, country, bank, name, codea, emoji
		except Exception as e:
			return ["No Found Data"]
		

	def time_taken(self):
		return round(time.perf_counter() - self.time, 2)

	def get_gateway(self):
		return self.gateway_name

	def get_card(self):
		return self.card

	def get_time(self):
		return self.time

	def set_card(self, card):
		self.card = card