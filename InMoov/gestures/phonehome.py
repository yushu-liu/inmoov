def phonehome():
  relax()
  i01.startedGesture()
  sleep(1)
  i01.setHeadVelocity(-1,-1,-1,-1,-1)
  i01.setArmVelocity("left",-1.0,-1.0,-1.0,-1.0)
  i01.setArmVelocity("right",-1.0,-1.0,-1.0,-1.0)
  i01.setHandVelocity("left",-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
  i01.setHandVelocity("right",-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
  i01.setTorsoVelocity(-1.0,-1.0,-1.0)
  i01.moveHead(160,68)
  i01.moveArm("left",5,86,30,20)
  i01.moveArm("right",86,140,83,80)
  i01.moveHand("left",99,140,173,167,130,26)
  i01.moveHand("right",135,6,170,145,168,180)
  i01.moveTorso(25,80,90)
  sleep(2)
  #i01.mouth.speakBlocking("E,T phone the big home of the inmoov nation")
  AudioPlayer.playFile(RuningFolder+'/system/sounds/E,T phone the big home of the inmoov nation.mp3')
  sleep(2)
  i01.finishedGesture()
  rest()
  sleep(1)
  relax()