import os, sys, time

from discord_webhook import DiscordWebhook

class Discord:
	def send_news(msg):
		msg = f"{msg}"
		try:
			webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1368789768074166433/3e3Ttm_4rQajcKK0gUTU_uZs5F8y2Oluz1NgbzzE5s45e-Kj5x_emRqNZLvfVGRBeF3T', content=msg)
			webhook.execute()
			print("sent")
		except:
			print("Failed to send discord notification!")
		return ""

	def send_status(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1368789768074166433/3e3Ttm_4rQajcKK0gUTU_uZs5F8y2Oluz1NgbzzE5s45e-Kj5x_emRqNZLvfVGRBeF3T', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_attack(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1368789768074166433/3e3Ttm_4rQajcKK0gUTU_uZs5F8y2Oluz1NgbzzE5s45e-Kj5x_emRqNZLvfVGRBeF3T', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_login(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1368789768074166433/3e3Ttm_4rQajcKK0gUTU_uZs5F8y2Oluz1NgbzzE5s45e-Kj5x_emRqNZLvfVGRBeF3T', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_logs(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1368789768074166433/3e3Ttm_4rQajcKK0gUTU_uZs5F8y2Oluz1NgbzzE5s45e-Kj5x_emRqNZLvfVGRBeF3T', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")
