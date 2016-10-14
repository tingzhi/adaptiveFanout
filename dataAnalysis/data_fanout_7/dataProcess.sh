#!/bin/bash

for i in `seq 10 10 200`;
do	
	mkdir "brTime_$i"
done

for i in `seq 10 10 200`;
do
	#echo brTime_$i_*.txt
	echo $i
	mv brTime_"$i"_*.txt brTime_"$i"	
done

mkdir energy lifeSpan overhead
mv overhead_*.txt overhead
mv energy_*.txt energy
mv lifeSpan_*.txt lifeSpan
