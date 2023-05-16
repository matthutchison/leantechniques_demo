default:
	docker build -t leantechniques-demo .

test: default
	docker run -it --rm leantechniques-demo python3 -m unittest

run: default
	docker run -it --rm leantechniques-demo