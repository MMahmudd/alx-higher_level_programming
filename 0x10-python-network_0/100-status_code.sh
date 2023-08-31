#!/bin/bash
# sends_a_request_to_a_URL, 
# and_displays_only_the status_code of_the_response.
curl -s -o /dev/null -w "%{http_code}" "$1"
