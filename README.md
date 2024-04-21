# A Way To Convert Oobabooga Chat Logs Into Multiturn Data.

Basically, just download the script and then replace line 24's string with your Oobabooga chatlog folder.

Then, replace line 27's string with a jsonl file you intend to use for the reformatted interactions.

Finally. Run `python3 Convert.py` if you're on linux, or `python Convert.py` if you're on windows. You might need to copy the path for the script if you don't open your terminal into the folder where you downloaded it.
