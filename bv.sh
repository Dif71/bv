#!/bin/bash

cd /root/bv

[ -d "/root/bv/d" ] && rm -rf /root/bv/d
git clone https://github.com/Dif71/d.git
sudo cp -r d/* /root/bv/

dts=$(less d.txt)
refs=$(less rf.txt | shuf | sed -e ':a;N;$!ba;s/\n/,/g')
prxs=$(less px.txt | shuf | sed -e ':a;N;$!ba;s/\n/,/g')
IFS=', ' read -r -a dt <<< "$dts"
IFS=', ' read -r -a refe <<< "$refs"
IFS=', ' read -r -a prxe <<< "$prxs"

arrIN=(${dts//|/ })
dom=${arrIN[0]}
go=${arrIN[1]}

tref=${#refe[@]}
tprx=${#prxe[@]}

if [ "$go" == "s" ]; then
	cou=1
	for prx in "${prxe[@]}"
	do
		idx=$(($cou % $tref))
		while :; 
		do 
			if [ -f st.txt ]; then
				rm -rf st.txt 
				python3.8 crawl.py -t "$dom" -r "${refe[$cou-1]}" -p "$prx"
				break
			else
				echo "waiting job finish"
			fi
		done
		dly=$(shuf -i 3-10 -n 1)
		sleep "$dly"
		((cou++))
	done	
	echo "[Done]"

elif [ "$go" == "p" ]; then
	cou=1
	for prx in "${prxe[@]}"
	do
		idx=$(($cou % $tref))
		# echo "$cou. $prx"
		echo "$cou. python3.8 crawl.py -t $dom -r ${refe[$idx]} -p $prx"
		# python3.8 crawl.py -t "$dom" -r "${refe[$cou-1]}" -p "$prx"
		
		dly=$(shuf -i 3-10 -n 1)
		# echo "$dly"
		# sleep 3
		((cou++))
	done

else
	echo "Set par 2!"
	exit 0
fi

echo ""
echo -e " == [\e[32mCompleted\e[0m] == "
echo ""
