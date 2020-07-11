python3 qcode.py

python3 merge.py

ffmpeg -r 1/1 -pattern_type glob -i './video/*.png' -s 200x200 -sws_flags neighbor -c:v libx264 -vf fps=25 -pix_fmt yuv420p latencia.mp4