# AP-Itemization-Analysis

This was an entry for Riots API Contest 2.0. It gathers data from 400,000 league of legends matches; Half from before the AP items rework and half from after the rework. It then processes this data and produces 2 json files containing data of how the AP items were uses. One json file for before the rework and one for after the rework.

The JSON files contain the following data:
<ul>
<li>For each Item:
<ul>
  <li>Win Rate</li>
  <li>Order it was bought in (1st, 2nd etc.) (only for big items)</li>
</ul>
</li>
<li>
For each Champion:
<ul>
  <li>First back buy</li>
  <li>Most common AP items</li>
</ul>
</li>
</ul>

# How to reproduce results

<b>Dependencies:</b>
All scripts use python 3

The only dependency is the Requests module which can be installed using ```pip install requests```

<ol>

<li> Download .zip and extract it. You only need the files 'pulldata.py' 'helperfunctions.py', 'league.py', 'processdata.py' and the directory 'AP_ITEM_DATASET'. All other files included in the zip are outputs of these 3 files. </li>
<li> Run ```python3 pulldata.py```. This will gather data for all 400,000 matches and put them in a directory called 'chunks'. 'pulldata.py' makes use of functions and classes in 'helperfunctions.py' and 'league.py'. <li>
<li> Run ```python3 processdata.py```. This will process all the data gathered into the 'chunks' directory and put them all the resulting two json files in a directory called 'final'. </li>
</ol>

#Presentation on results

I did not make a website or any way for the results to be viewed to the view. The only way to view the results by reading the json files directly. 

I imagine one could make a very appealing UI to view the results using Google charts / bokeh / etc.
