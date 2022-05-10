# Get-TubeArchivist-Meta

Simple python script to extract the metadata that [TubeArchivist](https://github.com/bbilly1/tubearchivist) stores in Elastic.

My use case is to download youtube channels for my kids to watch via Emby. I am pulling the title, description, date published and youtube id. I then toss that in to an NFO file that Emby can use along with downloading the video thumbnail. 

Thank you to [bbilly1](https://github.com/bbilly1) for all the great work on TubeArchivist. 

## Use with environment variables

This script can be run with the following variables set:

- `ES_USERNAME` - a username for connecting to ElasticSearch (ex: `elastic`)
- `ES_PASSWORD` - a password for connecting to ElasticSearch (ex: `verysecret`)
- `ES_SERVER_ADDR` - a full address including port for ElasticSearch (ex: `192.168.7.221:9200`)

These values can be passed directly or provided by a `.env` file. To use the included one please `cp .env-example .env` and fill out your values in `.env`

## Usage:
configure your path and server and run. it will scan the path for files, pull the youtubeid out and search elastic for the metadata and write it a file matching the video file name. 
