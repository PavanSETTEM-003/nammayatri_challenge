# nammayatri_challenge

The Telegram Bot is a proposed auto booking system that aims to simplify the process of booking, particularly for users who may not be tech-savvy or only have the location of their destination. To book an auto through the bot, users simply need to share their destination location with the bot, which then prompts the user to share their current location through the "share location" button. Once the bot has both the user and destination location, it displays them to the user for confirmation.

If the user needs to correct any mistakes in the location or swap the user and destination location, the bot offers buttons to do so. Once the booking is confirmed, the bot sends a JSON request to the Nammayatri booking system for fare and booking details. The API result is then sent to the user as a booking confirmation message, which includes the driver's name, contact number, auto number, fare, and estimated arrival time.

The prototype for the Nammayatri Telegram Bot in the name "nammayatri_prototype".I welcome any feedback and suggestions for future development, your input is valuable in improving the functionality and usability of the bot, and I am open to discussing any ideas you may have."

Telegram bot link: https://t.me/Nammayatri_prototype_bot

![all20one](https://user-images.githubusercontent.com/88257205/235337313-4f9afcb9-4699-455d-bd6f-2dfb9549ad39.png)

<h3>To make a similar bot, please follow these steps:</h3>
<ol>
<li>Open Telegram and search for BotFather in the search bar.</li>
<li>Start a chat with BotFather by clicking on the BotFather profile and then clicking the "Start" button.</li>
<li>Send the message "/newbot" to BotFather to create a new bot.</li>
<li>BotFather will ask you to choose a name for your bot. Choose a name and send it to BotFather.</li>
<li>BotFather will then ask you to choose a username for your bot. This username must end with the word "bot". For example, if your bot's name is "Test Bot", your username could be "testbot" or "test_bot".</li>
<li>Once you have chosen a username, BotFather will send you a message containing your bot's API token. This token will be a long string of letters and numbers.</li>
<li>Note down the API token as you will need it later in the code.</li>
<li>Now that you have your bot's API token, open the telegram.py code Replace the word "TOKEN_ID" in your code with your actual API token.</li>
<li>To access the bot, simply run the code and the bot will be up and running. Users can now search for the bot using its username and start interacting with it.
</li>
</ol>


In addition to the Telegram Bot, it is suggested that a similar booking option could be introduced on WhatsApp. This could greatly benefit users by expanding the reach and accessibility of the Nammayatri service. Given the popularity of WhatsApp in India, introducing a similar booking option in WhatsApp could lead to increased usage of the Nammayatri service and a better user experience overall.
