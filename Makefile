run:
	python ./MyPackages/main.py

clean:
	if exist "./_pychache_" rd /s /q _pycache_
	if exist "./DICE_GAME.egg-info" rd /s /q DICE_GAME.egg-info

#clean:
#	if exist "./_pychache_" rd /s /q _pycache_
#	if exist "./DICE_GAME.egg-info" rd /s /q DICE_GAME.egg-info

test:
