# user-authentication-using-voice-biometrics
Project involving Voice Signal Processing of users to recognise them using Voice Biometrics

1. scikit-learn
2. scikits.talkbox
3. pyssp
4. PyQt4
5. PyAudio
6. Python bindings for bob
	
In order to use `fast-gmm` instead of `sklearn.mixture.GaussianMixture` :
  run `make -C gmm/` in terminal to configure your system for fast-gmm
  
In order to run the application in command line :
1. Train:
python `__init__.py` -t enroll
2. Prediction:
python `__init__.py` -t predict
    
NOTE : Put all the wavfiles in the directory mentioned in the __init__.py file (for both training and prediction) and can be modifies accordingly.
