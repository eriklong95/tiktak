# tiktak-client
A client app for the tiktak platform built with React

## How to run
You need to have Node.js installed to run the project.

Clone the project, then `cd` to the project's root directory. 

Install `react-scripts` by running
```
npm install react-scripts@latest
```

Then run the command
```
npm start
```
The app should now be running on `http://localhost:3000`.

## tiktak server
The code for the tiktak server can be found here: https://github.com/eriklong95/tiktak.

## Proxy backend
The app is set up in a way such that HTTP requests will hit a proxy server running on the same host
and port. In `package.json` you can configure where that proxy should redirect the calls. As an
example, if `package.json` has
```JSON
"proxy": "http://host:1234" 
```
a call to `fetch('/users')` from the app will end up as a request to `http://host:1234/users`.