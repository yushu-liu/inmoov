# ##############################################################################
# 								EAR SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

python.subscribe(ear.getName(),"recognized")

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

# this function catch the ear listening
def onRecognized(text):
	if DEBUG==1:
		print "onRecognized : ",text

# ##############################################################################
# EAR RELATED FUNCTIONS
# ##############################################################################