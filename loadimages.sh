#!/bin/bash

dot -Tsvg chess.dot -o ./images/chess.svg
dot -Tpng chess.dot -o ./images/chess.png
