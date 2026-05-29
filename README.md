# contact merging script
- takes in contacts from various sources and merges them all into one file to be imported or used in any way you want.
  - Currently merges if names are the same. perhaps an algorithm can be used to decide if contacts are unique or not?
---
## how to use
- you need python and dependencies installed you can then run using the terminal or any ide of your choice
  - will consider adding venv for user convenience
---
## supported types
- vcf (virtual contact file)
- more soon
---
## current limits
- merges based off name only could merge two people that have the same name
- creates db file with merged contact list have not implemented conversion back to vcf
---
## requirements
- vobject
- sqlite3
- python 3.11 (untested with older versions)

