#!/bin/bash

#cd data

for i in `seq 10 40 90`;
do
	#echo brTime_$i_*.txt
	echo $i
	mkdir brTime_"$i"
	mv brTime_"$i"_*.txt brTime_"$i"	
done

mkdir brTime_150
mv brTime_150_*.txt brTime_150

mkdir energy lifeSpan overhead
mv energy_*.txt energy
mv lifeSpan_*.txt lifeSpan
mv overhead_*.txt overhead
