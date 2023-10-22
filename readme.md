Created this project in python by first creating a python environment:
```
python3 -m venv venv
source env/bin/activate
python3 -m pip install -r requirements.txt
```

Then you can drop in whatever image you want and run mobile_net.py like this:
```
python3 mobile_net.py
```

The output will be the probability of what was found in the image (using imagenet weights):
(e.g. for the picture of a nail)
```
1/1 [==============================] - 1s 661ms/step
1: nail (0.75)
2: screw (0.04)
3: ballpoint (0.04)
4: hook (0.02)
5: corkscrew (0.02)
```