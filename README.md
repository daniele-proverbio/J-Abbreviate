# J-Abbreviate
Shortener of scientific journal names.

## Scope
Often, scientific journals ask the bibliography to include the abbreviated version of referenced journal names (e.g. Journal of Theoretical Biology --> J Theo Biol). 
This little program automatises the process, by providing the abbreviation of journal names or substituting bibliography entries in .bib files.

## Use
Simply download `JournalNameAbbr.py` and run it from any terminal using _python3_.  
Two functions are available: entering a single journal name or a file to process.  
After the desired function is selected, follow the instructions.

### Processing a bibliography file
The code processes bibliography files written in [.bib](https://www.bibtex.org/) style. However, I could not find a .bib parser that suited the programming needs, hence this code works with .txt files.  
Therefore, make this **extra manual step**: copy-paste your .bib file content into a .txt, run the program, and copy-paste the output _shortBib.txt_ file back into a .bib

## Example
Say you have a .bib file with the following entry:

```
@article{myAuthor2023,
	title={A very nice paper written by someone important},
	author={Author, My},
	journal={Journal of Impressive Science},
	volume={1},
	number={1}
	pages={1},
	year={2023},
}
```
- Copy-paste this content into a _references.txt_ file
- In a terminal window, `>> python3 JournalNameAbbr.py`
- Select to get a single journal name (1) or to parse the whole references file (2)
- If you chose 1, type the journal name
- If you chose 2, provide the path to the _references.txt_ file
- Run it. If multiple journals bear similar names, you will be asked to select the one you want
- Get the  _shortBib.txt_ in the same folder as your original file (that is kept for future usage). Its  _journal_ entries have been shortened.
- Copy-paste its content in a .bib file to link it to your LaTex documents

## Disclaimers
- This program browses the dictionary database [Web of Knowledge](https://images.webofknowledge.com/images/help/WOS/0-9_abrvjt.html) to get its entries. If you are unsure about some result, please visit the original website. Any credits for curating the dictionary goes to it.
-  This is version 0.1: a simple code with no installation or fancy curation. It is primarily intended to support researchers in their manuscript proofing. If you'd like to improve it, extend it or embed it into Open Source softwares, please open a pull request and/or get in touch (daniele.proverbio@unitn.it).
-  If you like this little program, consider starring it :)
