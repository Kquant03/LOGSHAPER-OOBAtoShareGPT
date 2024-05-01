# A Way To Convert Oobabooga Chat Logs Into Multiturn Data.

LOGSHAPER is an initiative to take all of the work I've done in [OOBA](https://github.com/oobabooga/text-generation-webui) and convert those interactions to trainable formats.

Basically, just download the script and then replace line 24's string with your Oobabooga chatlog folder.

![image](https://github.com/Kquant03/LOGSHAPER-OOBAtoShareGPT/assets/155934148/de1a41cd-43f7-4895-804b-54d53b599862)

Then, replace line 27's string with a jsonl file you intend to use for the reformatted interactions.

![image](https://github.com/Kquant03/LOGSHAPER-OOBAtoShareGPT/assets/155934148/497b671f-9890-4c26-964f-560ed9eda511)

Finally. Run `python3 Convert.py` if you're on linux, or `python Convert.py` if you're on windows. You might need to copy the path for the script if you don't open your terminal into the folder where you downloaded it.
