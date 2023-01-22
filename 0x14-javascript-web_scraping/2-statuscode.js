t url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else console.log('code:', response && response.statusCode);
});
