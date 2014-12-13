#!/bin/bash

echo 'svg begin'
dot -Tsvg chess.dot -o ./images/chess.svg
echo 'svg complete'

echo 'png begin'
dot -Tpng chess.dot -o ./images/chess.png
echo 'png complete'

echo 'svg begin'
dot -Tsvg le.dot -o ./images/color.svg
echo 'svg complete'

echo 'png begin'
dot -Tpng le.dot -o ./images/color.png
echo 'png complete'
