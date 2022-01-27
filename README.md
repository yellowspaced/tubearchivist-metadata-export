# Get-TubeArchivist-Meta

Simple python script to extract the metadata that [TubeArchivist](https://github.com/bbilly1/tubearchivist) stores in Elastic.

My use case is to download youtube channels for my kids to watch via Emby. I am pulling the title, description, date published and youtube id. I then toss that in to an NFO file that Emby can use along with downloading the video thumbnail. 

Thank you to [bbilly1](https://github.com/bbilly1) for all the great work on TubeArchivist. 

Usage:
configure your path and server and run. it will scan the path for files, pull the youtubeid out and search elastic for the metadate and write it a file matching the video file name. 
