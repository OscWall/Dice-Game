.PHONY: test clean doc uml
test: 
	python test_dice.py
	python test_diceHand.py
	python test_player.py
	python test_intelligence.py

run:
	python main.py

clean:
	if exist "./_pychache_" rd /s /q _pycache_
	if exist "./DICE_GAME.egg-info" rd /s /q DICE_GAME.egg-info

install:
	pip install -r requirements.txt


doc:
	for file in *.py; do \
		module=$${file%.py}; \
		module=$${module////.}; \
		python -m pydoc -b $$module; \
	done
	
lint:
	flake8 .
	pylint *.py

pyreverse:
	install -d doc/pyreverse
	pyreverse *.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot