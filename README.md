# Happybot
A positive discord bot meant to send people positive words of affirmation and say nice things

# How to use
Simply run the python 3.8 script somewhere with the cloned repository.

Current supported commands:

* !kindwords

This will reply to the user with random kind words of affirmation

* !sendkindwords @user

This will send the tagged user random words of affirmation privately

* !encourage

The bot will post a random inspirational quote to the channel

* !lottery

Feeling generous?  Want to hand out some free keys to users from steam?
Do you want to make sure it doesn't accidentally make people fight over them?
Want to make sure people don't get locked out?
Well, every time someone does "!lottery" it will private message them a key.
It will then add them to the lotteryclaims.txt file.
keysclaimed.txt will then be updated, and moved from keysactive.txt.

So simply add any active keys to keysactive.txt.  The lottery will randomly pluck one,
give it to a user, add that key to the list of used keys, and users claimed, and
now everyone has a chance to win the lottery!

If you want to truly make it even more random where maybe they do or don't get one
you can add bogus fake keys or messages in the keysactive.txt as it literally just cuts
and pastes the contents from one file to the other.

Want 10 keys and 100 lines?  Put them in the first 10 lines and then have 90 lines of
lorem ipsum.  Be creative, have fun.
