# pibsite
Website for PIB project

Uses the webssh client: https://github.com/huashengdun/webssh

Repo for the website: https://github.com/eevelweezel/pibsite

Create a python 3.10 venv

Run: pip install -r requirements.txt

From the root directory, run:
    wssh

    ./manage.py runserver


Currently, we're seeing:

Firefox Can’t Open This Page

To protect your security, 127.0.0.1 will not allow Firefox to display the page if another site has embedded it. To see this page, you need to open it in a new window.

Learn more…

Report errors like this to help Mozilla identify and block malicious sites


We need to fix CORS/nginx to fix the cross-origin stuff.
