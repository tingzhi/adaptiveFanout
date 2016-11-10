#!/bin/bash

#cd data

for i in `seq 10 40 210`;
do
	#echo brTime_$i_*.txt
	echo $i
	mkdir brTime_"$i"
	mv brTime_"$i"_*.txt brTime_"$i"	
done


mkdir energy lifeSpan overhead
mv energy_*.txt energy
mv lifeSpan_*.txt lifeSpan
mv overhead_*.txt overhead
