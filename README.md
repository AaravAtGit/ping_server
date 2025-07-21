# Ping Server
================

A server to receive heartbeats from client machines

## Overview
-----------

The Ping Server is a simple Flask-based server that receives periodic "heartbeats" from client machines. The server keeps track of the last seen time for each client and can be configured to send notifications when a client goes offline.

## Features
------------

* Receives POST requests from clients at the `/alive/<computer>` endpoint
* Keeps track of the last seen time for each client in a JSON file (`computers.json`)
* Sends notifications when a client goes offline for more than 5 seconds

## Configuration
---------------

The server uses a JSON file (`computers.json`) to store the list of whitelisted clients and their last seen times. The file is located in the `src/ping_server` directory.

## Running the Server
---------------------

To run the server, navigate to the `src/ping_server` directory and execute the `app.py` file using Python:
```bash
python app.py
```
The server will start listening on port 5000.

## API Endpoints
----------------

### `/alive/<computer>`

* Method: POST
* Description: Receive a heartbeat from a client machine
* Parameters:
	+ `computer`: The name of the client machine

## Example Use Case
--------------------

To send a heartbeat from a client machine, use a tool like `curl` to send a POST request to the `/alive/<computer>` endpoint:
```bash
curl -X POST http://localhost:5000/alive/my_computer
```
This will update the last seen time for the `my_computer` client in the `computers.json` file.

## License
----------

This project is released under the [GNU General Public License](LICENSE).