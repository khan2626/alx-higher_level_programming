#!/usr/bin/node

request = require('request');
fs = require('fs')
const url = process.argv[2];
const file_path = process.argv[3];

request.get(url, (error, resp, body) => {
	if (error) {
		console.log(error);
	}
	else {
		fs.writeFile(file_path, body, 'utf-8', (error) => {
			if (error) {
				console.log(error);
			}
		});
	}
});