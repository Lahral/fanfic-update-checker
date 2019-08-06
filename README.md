# Fanfic-update-checker
Checks to see if there is a new update for a fanfic hosted on fanfiction.net

## About
This works in two stages: 
*  The CSV document that contains the list of fanfictions and necessary information
*  The python script that runs the code.


### The CSV file:

Comes in the form of:
name, fanfic ID, chapter number, Author ID, xudate of last update

Author ID is only used in case the fanfic is pulled, or there is an issue 
preventing access to the fanfic at the current moment. At least with the Author 
ID, you can visit the author's page to see what happened/regain access to the story.

### The python script:

Uses requests to gather the html from fanfiction.net for the selected chapter,
then uses RegEx to search for the part of the page where the last update is 
stored.

Only works with fanfics from fanfiction.net, for the time being. 

## Use:

When adding in the new fanfiction to the csv file, set LAST UPDATE to 0, and 
enter the second to latest chapter. When run, both the LAST UPDATE and chapter 
will be updated to the current values.

## Current Issues:

* ~~If placing a fanfic with no updates, will crash due to edge cases with RegEx.
 Will be fixed shortly.~~ 
 With a simple fix, this isn't really an issue, and makes some sense since it 
 technically hasn't been updated yet
