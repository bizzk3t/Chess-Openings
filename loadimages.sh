#!/bin/bash

echo 'svg begin'
dot -Tsvg chess.dot -o ./images/chess.svg
echo 'svg complete'

echo 'jpg begin'
dot -Tjpg chess.dot -o ./images/chess.jpg
echo 'jpg complete'

echo 'png begin'
dot -Tpng chess.dot -o ./images/chess.png
echo 'png complete'
