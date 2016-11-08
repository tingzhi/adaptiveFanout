#!/bin/bash

#cd data

for i in `seq 10 40 90`;
do
	#echo brTime_$i_*.txt
	echo $i
	mv brTime_"$i"_*.txt brTime_"$i"	
done

mv brTime_150_*.txt brTime_150
