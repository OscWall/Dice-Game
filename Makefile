run:
	python Dice-Game/main.py

install:
	pip install -r requirements.txt

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./DICE_GAME.egg-info" rd /s /q DICE_GAME.egg-info