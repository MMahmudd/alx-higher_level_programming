#!/bin/bash
# send_a_POST request to_the_passed URL using_curl,
# and_display_the body_of_the_response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
