reset
fontSpec(s) = sprintf("Arial, %d", s)
fontSpecBold(s) = sprintf("Arial Bold, %d", s)

set terminal pngcairo nocrop enhanced font fontSpec(14)

set key box top left spacing 1

set ylabel "Time of CPU Usage (seconds)" font fontSpecBold(14)
set xlabel "IoMT APP Number" font fontSpecBold(14)

set ytics format "{/:Bold {/=14 %h}}"
set xtics font "Arial Bold, 14" 

# Replace small stripes on the Y-axis with a horizontal gridlines
set tic scale 1
set grid ytics lc rgb "#000000"

# Remove border around chart
# unset border

# Manual set the Y-axis range
set yrange [0 to 90]

set output "6.png"

set boxwidth 1

y1 = 0
y2 = 0

f1(x) = (y1 = y1*0.95)
f2(x) = (y2 = y2*0.95)

set style histogram errorbars gap 1 lw 1
set style data histograms
set style fill solid 1.00 border 0
set bars 0.5

plot "cpu.dat" using 2:2:xtic(1) lt rgb "#0000ff" t "V-PRISM Approach", \
            "" using 3:3 lt rgb "#ff0000" t "Traditional Approach"