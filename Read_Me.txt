####################################
########## App Issue 1 #############
####################################


On this branch the app appears to work correctly, but once it's up and running the graphs on localhost:5000 won't load.

To get these visuals to load I need to move some of the app and server code out of the index.py and into a separate app.py.
The branch 'App Issue 2' separates out the app and server code into it's own app.py.

Also on this branch, the Dockerfile runs the container with 'CMD ["python3", "index.py"]'.
I'm pretty sure for this to be productionised it needs to use the commented out code:
'CMD gunicorn --bind 0.0.0.0:5000 --workers=3 --threads=3 index:server'
The branch 'App Issue 3' uses this code to run the container .
